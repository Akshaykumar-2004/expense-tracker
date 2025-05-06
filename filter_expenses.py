import csv

def filter_expenses(file_path):
    print("\n===== FILTER EXPENSES =====")
    print("Filter by:")
    print("1. Category")
    print("2. Date (YYYY-MM-DD)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        category = input("Enter category to filter by: ").strip()
        filter_by_column(file_path, "Category", category)

    elif choice == '2':
        date = input("Enter date to filter by (YYYY-MM-DD): ").strip()
        filter_by_column(file_path, "Date", date)

    else:
        print("Invalid choice.")

def filter_by_column(file_path, column_name, value):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            filtered = []

            for row in reader:
                file_value = row[column_name].strip()
                input_value = value.strip()

                # Print debug output
                print(f"[DEBUG] Comparing file '{file_value}' with input '{input_value}'")

                if column_name == "Date":
                    if file_value == input_value:
                        filtered.append(row)
                else:
                    if file_value.lower() == input_value.lower():
                        filtered.append(row)

            if filtered:
                print("\nFiltered Expenses:")
                print("{:<12} {:<10} {:<15} {}".format("Date", "Amount", "Category", "Description"))
                print("-" * 55)
                for row in filtered:
                    print("{:<12} {:<10} {:<15} {}".format(row['Date'], row['Amount'], row['Category'], row['Description']))
            else:
                print(f"No expenses found for {column_name.lower()} '{value}'.")

    except FileNotFoundError:
        print("Expense file not found. Please add expenses first.")

