import csv
from collections import defaultdict
from datetime import datetime

def view_summary(file_path):
    """View detailed summary of all expenses"""
    print("\n===== EXPENSE SUMMARY =====")

    # Initialize counters and data structures
    total_expenses = 0                # Total number of expense entries
    total_amount = 0.0                # Total amount spent
    category_totals = defaultdict(float)  # Amount spent per category
    unique_dates = set()              # Set of unique dates for daily average

    try:
        # Open the CSV file for reading
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)  # Read CSV into dictionary format

            # Iterate through each expense record
            for row in reader:
                try:
                    amount = float(row["Amount"])         # Convert amount to float
                    date_str = row["Date"]                # Extract the date
                    category = row["Category"]            # Extract the category

                    total_amount += amount                # Add to total amount
                    total_expenses += 1                   # Increment expense count
                    category_totals[category] += amount   # Sum by category
                    unique_dates.add(date_str)            # Track unique dates
                except (ValueError, KeyError):
                    # Skip any rows with missing or invalid data
                    print(f"Skipping invalid entry: {row}")
    except FileNotFoundError:
        # Handle case where the CSV file doesn't exist
        print("No expense records found.")
        return

    # Determine category with highest total amount spent
    most_spent_category = max(category_totals, key=category_totals.get) if category_totals else "N/A"
    most_spent_amount = category_totals[most_spent_category] if category_totals else 0

    # Calculate daily average spending
    num_days = len(unique_dates)
    daily_average = total_amount / num_days if num_days > 0 else 0

    # Display overall summary
    print(f"\nTotal Expenses Recorded: {total_expenses}")
    print(f"Total Amount Spent: ₹{total_amount:.2f}")
    print(f"Most Spent On: {most_spent_category} (₹{most_spent_amount:.2f})")
    print(f"Daily Average Spending: ₹{daily_average:.2f}\n")

    # Display amount spent per category
    print("Amount Spent by Category:")
    for category, amount in category_totals.items():
        print(f"  {category}: ₹{amount:.2f}")

# If running this file directly, call the function on 'expenses.csv'
if __name__ == "__main__":
    view_summary("expenses.csv")
