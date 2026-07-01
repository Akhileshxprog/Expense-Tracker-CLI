import csv
from datetime import datetime
import argparse

# Saving Expenses in a CSV file

def save_expense(expenses):
    with open("expense.csv", "w", newline="") as file:
        fieldname = ["ID", "Date", "Description", "Amount"]
        csv_write = csv.DictWriter(file, fieldnames=fieldname)
        csv_write.writeheader()
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

    # "add" adding functionality for adding expense from terminal
    add_parser = subparser.add_parser("add")
    add_parser.add_argument("--description")
    add_parser.add_argument("--amount", type=float)

    # "list" adding functionality for viewing all expenses
    list_parser = subparser.add_parser("list")

    # "summary" adding functionality for viewing summary of all expenses
    summary_parser = subparser.add_parser("summary")
    summary_parser.add_argument("--month", nargs="?")

    args = parser.parse_args()

    # setting the load_expenses() to expenses
    expenses = load_expenses()

    # adding expense
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
    # printing the expenses
        print(expenses)

    # listing/printing all expenses
    elif args.command == "list":
        if len(expenses) != 0:
            print(expenses)
        else:
            print("Expenses file is empty")

    # printing summary
    elif args.command == "summary":
        if args.month == None:
            total_sum = 0
            for expense in expenses:
                total_sum += sum(expense["Amount"])
            print(total_sum)


expense_tracker()