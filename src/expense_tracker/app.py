from flask import Flask, redirect, render_template, request, url_for

from expense_tracker.models import (
    add_transaction,
    get_totals,
    get_transactions,
    init_db,
)

app = Flask(__name__)

# Ensure DB is initialized
init_db()


@app.route("/")
def index():
    transactions = get_transactions()
    total_income, total_expense, balance = get_totals()
    return render_template(
        "index.html",
        transactions=transactions,
        total_income=total_income,
        total_expense=total_expense,
        balance=balance,
    )


@app.route("/add", methods=["POST"])
def add():
    transaction_type = request.form.get("transaction_type")
    category = request.form.get("category")
    amount_str = request.form.get("amount")
    date = request.form.get("date")

    if not transaction_type or not category or not amount_str or not date:
        return "Invalid input", 400

    if transaction_type not in ["Income", "Expense"]:
        return "Invalid transaction type", 400

    allowed_categories = [
        "Food",
        "Transport",
        "Utilities",
        "Entertainment",
        "Shopping",
        "Miscellaneous",
    ]
    if category not in allowed_categories:
        return "Invalid category", 400

    try:
        amount = float(amount_str)
        if amount <= 0:
            return "Amount must be greater than 0", 400
    except ValueError:
        return "Invalid amount", 400

    add_transaction(transaction_type, category, amount, date)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
