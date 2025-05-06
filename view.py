import csv 
from collections import defaultdict  
from datetime import datetime 

def view_expenses(file_path):
    """Displays a summary of expenses from the CSV file"""
    print("\n EXPENSE SUMMARY")  # Print header for the summary output

    try:
        # Attempt to open the file at the provided file path
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)  # Create a CSV reader that maps rows to dictionaries
            # Filter out any invalid or empty rows, only keeping rows where all values are present
            expenses = [row for row in reader if row and all(row.values())]

            # Check if no valid expenses are found, if so, print message and exit
            if not expenses:
                print("No expenses recorded yet.")
                return

            total_expense = 0.0  # Initialize the variable to hold the total expense sum
            category_totals = defaultdict(float)  # Dictionary to hold total spending per category (default value is float, initialized to 0.0)
            date_set = set()  # Set to track unique dates for daily average calculation

            # Loop through all the expenses and process each row
            for row in expenses:
                try:
                    # Convert the "Amount" from string to float, extract category and date
                    amount = float(row["Amount"])
                    category = row["Category"]
                    date_str = row["Date"]

                    # Add the amount to the total expense
                    total_expense += amount
                    # Add the amount to the category's total in the category_totals dictionary
                    category_totals[category] += amount
                    # Add the date to the set of dates (ensures no duplicates)
                    date_set.add(date_str)
                except (ValueError, KeyError):  # Handle any ValueErrors or KeyErrors (e.g., if the row is malformed)
                    print(f"Skipping invalid row: {row}")  # Print message for invalid rows and skip them
                    continue

            # Calculate the category with the highest spending
            most_spent_category = max(category_totals, key=category_totals.get)
            most_spent_amount = category_totals[most_spent_category]  # Get the total for the most spent category

            # Calculate the number of unique days (length of date_set) for daily average calculation
            days_count = len(date_set)
            # Calculate the daily average spend, handle case where there are no days (to avoid division by zero)
            daily_average = total_expense / days_count if days_count > 0 else 0

            # Display the summary of expenses
            print(f"\nTotal Expenses     : ₹{total_expense:.2f}")  # Print total expenses
            print(f"Most Spent On      : {most_spent_category} (₹{most_spent_amount:.2f})")  # Print category with most spending
            print(f"Daily Average Spend: ₹{daily_average:.2f} over {days_count} day(s)")  # Print daily average spend

    except FileNotFoundError:  # Handle the case where the expenses file is not found
        print("No expenses file found. Please add expenses first.")  # Print an error message

# This section runs when the script is executed directly
if __name__ == "__main__":
    # Call the function to view expenses from the "expenses.csv" file
    view_expenses("expenses.csv")

          
           
