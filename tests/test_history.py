import os

import pytest

from expense_tracker.app import app
from expense_tracker.models import add_transaction, init_db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_history_table(client):
    if os.path.exists("expenses.db"):
        os.remove("expenses.db")

    init_db()
    add_transaction("Income", "Food", 100.0, "2026-09-19")

    rv = client.get("/")
    assert rv.status_code == 200
    assert b"2026-09-19" in rv.data
    assert b"Income" in rv.data
    assert b"Food" in rv.data
    assert b"100.0" in rv.data

    if os.path.exists("expenses.db"):
        os.remove("expenses.db")
