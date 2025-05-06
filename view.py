import csv
from collections import defaultdict

def view_expenses(file_path):
    """Displays a summary of expenses from a CSV file with no headers."""
    print("\n EXPENSE SUMMARY") #Shows the heading of view summary

    try:
        with open(file_path, 'r') as file: #opens the file in read mode
            reader = csv.reader(file)
            expenses = []

            for row in reader:
                # checks for empty or invalid rows
                if len(row) < 3:
                    print(f"Skipping invalid row: {row}")
                    continue
                expenses.append(row)

            if not expenses:
                print("No expenses recorded yet.") #prints if list is empty
                return

            total_expense = 0.0                    
            category_totals = defaultdict(float)   
            date_set = set()

            for row in expenses:
                try:
                    date = row[0]
                    amount = float(row[1])
                    category = row[2]
                    # Description (row[3]) is optional and unused here

                    total_expense += amount
                    category_totals[category] += amount
                    date_set.add(date)
                except (ValueError, IndexError):
                    print(f"Skipping invalid row: {row}")
                    continue

            # Find the category with the highest total spending
            most_spent_category = max(category_totals, key=category_totals.get)
            most_spent_amount = category_totals[most_spent_category]

            # Calculate average daily spend
            days_count = len(date_set)
            daily_average = total_expense / days_count if days_count > 0 else 0

            # Display summary
            print(f"\nTotal Expenses     : ₹{total_expense:.2f}")
            print(f"Most Spent On      : {most_spent_category} (₹{most_spent_amount:.2f})")
            print(f"Daily Average Spend: ₹{daily_average:.2f} over {days_count} day(s)")

    except FileNotFoundError:
        print("No expenses file found. Please add expenses first.")

if __name__ == "__main__":
    view_expenses("expenses.csv")

           
