from flask import Flask, render_template, request, redirect, url_for
from models import init_db, add_transaction, get_transactions

app = Flask(__name__)

# Ensure DB is initialized
init_db()

@app.route('/')
def index():
    transactions = get_transactions()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['POST'])
def add():
    transaction_type = request.form.get('transaction_type')
    category = request.form.get('category')
    amount = float(request.form.get('amount'))
    date = request.form.get('date')
    
    add_transaction(transaction_type, category, amount, date)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
