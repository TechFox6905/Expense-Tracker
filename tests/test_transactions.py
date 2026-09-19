from app import app
import pytest
import sqlite3
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_transaction(client):
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')
    
    # Initialize DB for the test
    from models import init_db
    init_db()
    
    rv = client.post('/add', data={
        'transaction_type': 'Income',
        'category': 'Food',
        'amount': 100.0,
        'date': '2026-09-19'
    }, follow_redirects=True)
    
    assert rv.status_code == 200
    
    # Verify in DB
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions;")
    transaction = cursor.fetchone()
    assert transaction is not None
    assert transaction[1] == 'Income'
    assert transaction[2] == 'Food'
    assert transaction[3] == 100.0
    assert transaction[4] == '2026-09-19'
    conn.close()
    
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')
