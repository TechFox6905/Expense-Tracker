from app import app
import pytest
import sqlite3
import os
from models import init_db, add_transaction

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dashboard_summary(client):
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')
    
    init_db()
    add_transaction('Income', 'Food', 100.0, '2026-09-19')
    add_transaction('Expense', 'Food', 50.0, '2026-09-20')
    
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Total Income' in rv.data
    assert b'100.0' in rv.data
    assert b'Total Expense' in rv.data
    assert b'50.0' in rv.data
    assert b'Balance' in rv.data
    assert b'50.0' in rv.data
    
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')

def test_summary_update_after_transaction(client):
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')
    init_db()
    
    # Add initial
    client.post('/add', data={'transaction_type': 'Income', 'category': 'Food', 'amount': 100.0, 'date': '2026-09-21'})
    
    # Check
    rv = client.get('/')
    assert b'100.0' in rv.data
    
    # Add second
    client.post('/add', data={'transaction_type': 'Income', 'category': 'Food', 'amount': 50.0, 'date': '2026-09-22'})
    
    # Check updated
    rv = client.get('/')
    assert b'150.0' in rv.data # Income 100 + 50 = 150
    
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')
