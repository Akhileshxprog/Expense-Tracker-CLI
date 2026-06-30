import csv
from datetime import datetime
import argparse

# Saving Expenses in a CSV file

# def save_expense(expenses):
#     with open("expense.csv", "w", newline="") as file:
#         fieldname = []
#         csv_write = csv.writer(file)
#         csv_write.writerow(["ID", "Date", "Description", "Amount"])
#         csv_write.writerows(expenses)

# Loading Expenses if expenses file is empty, returns a nothing

# def load_expenses():
#     try:
#         with open("expense.csv", "r", newline="") as file:
#             csv_read = csv.reader(file)
#             return [row for row in csv_read]
#     except FileNotFoundError:
#         return []

# Main code goes here insdide expense_tracker function

def expense_tracker():

    """Using argparse subparser for CLI"""

    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparser = parser.add_subparsers(dest="command")

    #