from flask import Flask, render_template, request, redirect
from datetime import datetime
from expenses import load_expenses, save_expenses, add_expense, delete_expense, total_spent, total_by_cat


app = Flask(__name__)
FILENAME = "samplerecord.json"


@app.route("/")
def home():
    expenses = load_expenses(FILENAME)
    total = total_spent(expenses)
    totals = total_by_cat(expenses)
    return render_template("index.html", expenses=expenses, total=total, totals=totals)


@app.route("/add", methods=["POST"])
def add():
    try:
        amount = float(request.form["amount"])
        category = request.form["category"]
        date = datetime.strptime(request.form["date"], "%Y-%m-%d").date()
        note = request.form["note"]

        expenses = load_expenses(FILENAME)
        expenses = add_expense(expenses, amount, category, date, note)
        save_expenses(expenses, FILENAME)
    except ValueError:
        pass  # bad input: just ignore it for now
    return redirect("/")


@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    try:
        expenses = load_expenses(FILENAME)
        expenses = delete_expense(expenses, index)
        save_expenses(expenses, FILENAME)
    except ValueError:
        pass
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
