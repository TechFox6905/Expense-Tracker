import os

import pytest

from expense_tracker.app import app
from expense_tracker.models import init_db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    if os.path.exists("expenses.db"):
        os.remove("expenses.db")
    init_db()
    with app.test_client() as client:
        yield client
    if os.path.exists("expenses.db"):
        os.remove("expenses.db")


def test_empty_state(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"No transactions" in rv.data
    assert b"Total Income" in rv.data
    assert b"0" in rv.data
