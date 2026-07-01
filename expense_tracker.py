import csv
from datetime import datetime
import argparse

# Saving Expenses in a CSV file

def save_expense(expenses):
    with open("expense.csv", "w", newline="") as file:
        fieldname = ["ID", "Date", "Description", "Amount"]
        csv_write = csv.DictWriter(file, fieldnames=fieldname)
        csv_write.writerows(expenses)

# Loading Expenses if expenses file is empty, returns  nothing

def load_expenses():
    try:
        with open("expense.csv", "r", newline="") as file:
            csv_read = csv.DictReader(file)
            return [row for row in csv_read]
    except FileNotFoundError:
        return []

# Main code goes here insdide expense_tracker function

def expense_tracker():

    """Using argparse subparser function for CLI"""

    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparser = parser.add_subparsers(dest="command")

    # "add" adding functionallity for adding expense from terminal
    add_parser = subparser.add_parser("add")
    add_parser.add_argument("--description")
    add_parser.add_argument("--amount", type=float)

    args = parser.parse_args()

    expenses = load_expenses()

    if args.command == "add":
        expense_data = {
            "ID": 1,
            "Date": datetime.now().strftime("%d-%m-%y"),
            "Description": args.description,
            "Amount": args.amount
        }
        expenses.append(expense_data)
        print("Expense Added")
        save_expense(expenses)

expense_tracker()