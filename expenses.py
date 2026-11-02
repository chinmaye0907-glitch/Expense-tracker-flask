import json
from datetime import datetime

filename = "samplerecord.json"


def load_expenses(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses, filename):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses, amount, category, date, note=""):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    expense = {"amount": amount,
               "category": category,
               "date": date.isoformat(),
               "note": note}
    expenses.append(expense)
    return expenses


def delete_expense(expenses, index):
    if index < 0 or index >= len(expenses):
        raise ValueError("Invalid index")
    expenses.pop(index)
    return expenses


def total_spent(expenses):
    return sum(expense["amount"] for expense in expenses)


def total_by_cat(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0)+expense["amount"]
    return totals
