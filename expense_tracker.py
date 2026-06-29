import csv
from datetime import datetime
import argparse

def save_expense(expenses):
        with open("expense.csv", "w", newline="") as file:
            csv_write = csv.writer(file)
            csv_write.writerow([])
            csv_write.writerows(expenses)


def load_expenses():
    try:
        with open("expense.csv", "r", newline="") as file:
            csv_read = csv.reader(file)
            for row in csv_read:
                load = (", ".join(row))
            return load
    except (FileNotFoundError):
        return []



def expense_tracker():