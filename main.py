# main.py
import os
import csv
from datetime import datetime

# Import modules for different functionalities
from add_expense import add_expense
# The following will be implemented by your teammates
from view_expenses import view_expenses
from filter_expenses import filter_expenses
from delete_expense import delete_expense
from view import view_summary

# File to store expense data
EXPENSE_FILE = "expenses.csv"

def initialize_file():
    """Create the expense file if it doesn't exist with proper headers"""
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])

def display_menu():
    """Display the main menu options"""
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses")
    print("4. Delete Expense")
    print("5. View Summary")
    print("6. Exit")
    print("==========================")

def main():
    """Main function to run the expense tracker"""
    initialize_file()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_expense(EXPENSE_FILE)
        elif choice == '2':
            try:
                view_expenses(EXPENSE_FILE)
            except NameError:
                print("This feature is not implemented yet.")
        elif choice == '3':
            try:
                filter_expenses(EXPENSE_FILE)
            except NameError:
                print("This feature is not implemented yet.")
        elif choice == '4':
            try:
                delete_expense(EXPENSE_FILE)
            except NameError:
                print("This feature is not implemented yet.")
        elif choice == '5':
            try:
                view_summary(EXPENSE_FILE)
            except NameError:
                print("This feature is not implemented yet.")
        elif choice == '6':
            print("Thank you for using the Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
