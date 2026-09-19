import os
import sqlite3

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


def test_add_transaction(client):
    rv = client.post(
        "/add",
        data={
            "transaction_type": "Income",
            "category": "Food",
            "amount": 100.0,
            "date": "2026-09-19",
        },
        follow_redirects=True,
    )

    assert rv.status_code == 200

    # Verify in DB
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions;")
    transaction = cursor.fetchone()
    assert transaction is not None
    assert transaction[1] == "Income"
    assert transaction[2] == "Food"
    assert transaction[3] == 100.0
    assert transaction[4] == "2026-09-19"
    conn.close()


def test_add_expense(client):
    rv = client.post(
        "/add",
        data={
            "transaction_type": "Expense",
            "category": "Transport",
            "amount": 50.0,
            "date": "2026-09-20",
        },
        follow_redirects=True,
    )

    assert rv.status_code == 200

    # Verify in DB
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE transaction_type = 'Expense';")
    transaction = cursor.fetchone()
    assert transaction is not None
    assert transaction[1] == "Expense"
    assert transaction[2] == "Transport"
    assert transaction[3] == 50.0
    assert transaction[4] == "2026-09-20"
    conn.close()


def test_invalid_transaction_type(client):
    rv = client.post(
        "/add",
        data={
            "transaction_type": "InvalidType",
            "category": "Food",
            "amount": 100.0,
            "date": "2026-09-23",
        },
        follow_redirects=True,
    )

    assert rv.status_code != 200

    # Verify not in DB
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE transaction_type = 'InvalidType';")
    assert cursor.fetchone() is None
    conn.close()


def test_invalid_amount_form_submission(client):
    # Submit zero amount
    rv = client.post(
        "/add",
        data={
            "transaction_type": "Income",
            "category": "Food",
            "amount": 0.0,
            "date": "2026-09-22",
        },
        follow_redirects=True,
    )

    assert rv.status_code != 200

    # Verify not in DB
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE date = '2026-09-22';")
    assert cursor.fetchone() is None
    conn.close()


def test_invalid_category(client):
    rv = client.post(
        "/add",
        data={
            "transaction_type": "Income",
            "category": "InvalidCategory",
            "amount": 100.0,
            "date": "2026-09-24",
        },
        follow_redirects=True,
    )

    assert rv.status_code != 200

    # Verify not in DB
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE category = 'InvalidCategory';")
    assert cursor.fetchone() is None
    conn.close()
