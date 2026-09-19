import sqlite3
import pytest
import os
from models import init_db

@pytest.fixture
def db():
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')
    init_db()
    yield
    if os.path.exists('expenses.db'):
        os.remove('expenses.db')

def test_db_init(db):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='transactions';")
    assert cursor.fetchone() is not None
    conn.close()
