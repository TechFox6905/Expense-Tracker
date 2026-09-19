import os
import sqlite3

import pytest

from expense_tracker.models import init_db


@pytest.fixture
def db():
    if os.path.exists("expenses.db"):
        os.remove("expenses.db")
    init_db()
    yield
    if os.path.exists("expenses.db"):
        os.remove("expenses.db")


def test_db_init(db):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='transactions';"
    )
    assert cursor.fetchone() is not None
    conn.close()


def test_persistence(db):
    from expense_tracker.models import add_transaction, get_transactions

    add_transaction("Income", "Food", 100.0, "2026-09-19")

    # Re-fetch to ensure it is in DB
    transactions = get_transactions()
    assert len(transactions) == 1
    assert transactions[0][1] == "Income"

    # Manually re-read from a new connection to simulate restart
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    row = cursor.fetchone()
    conn.close()

    assert row is not None
    assert row[1] == "Income"
    assert row[3] == 100.0
