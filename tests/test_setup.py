from app import app
import pytest
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

def test_index(client):
    rv = client.get('/')
    assert b'<h1>Expense Tracker</h1>' in rv.data
    assert rv.status_code == 200
