from app import app
import pytest
import sqlite3
import os
from models import init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')
    init_db()
    with app.test_client() as client:
        yield client
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')

def test_add_transaction(client):
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
