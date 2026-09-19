from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert b'<h1>Expense Tracker</h1>' in rv.data
    assert rv.status_code == 200
