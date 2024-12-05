import time
import sys
import os
import pandas as pd  # Import pandas
from os.path import exists

expenses = []
currency = 'kr'
excel_file = 'Expense_2024.xlsx'  # Name of the Excel file to save/load expenses


# Clear terminal
def clear_term():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_term()


# Function to show progress bar
def progress_bar(steps, prefix='Processing', length=30):
    for i in range(steps):
        time.sleep(0.1)
        percent = (i + 1) / steps
        filled_length = int(length * percent)
        bar = '█' * filled_length + '_' * (length - filled_length)
        sys.stdout.write(f'\r{prefix}|{bar}|{int(percent * 100)}%')
        sys.stdout.flush()


while True:
    print(f"\n======================|Expense Tracker|=====================")
    print(f"\n=========================|Main Menu|========================")
    time.sleep(1)
    user_available_action = ['add', 'view', 'total', 'exit', 'view excel', 'total excel']
    user_chosen_action = input(f"\nChoose an action {user_available_action}: ").lower().strip()
    print("\n")

    if user_chosen_action == 'add':
        clear_term()  # Clear the terminal before each action
        print(f"\n===============|Adding item to Expense list|===============")
        time.sleep(1)
        while True:
            user_input = input("\nEnter an item and its price (eg., coffee 10):").split()
            print("\n")

            if len(user_input) != 2:
                print("Invalid input. Please provide both item name and price (eg., coffee 10).")
                time.sleep(1)
                continue
            add_item = user_input[0].capitalize()
            if not add_item.isalpha():
                print(
                    "Invalid item name. Please enter a valid string (letters only, no numbers or special characters).")
                time.sleep(1)
                continue

            try:
                add_value = float(user_input[1])
                if add_value <= 0:
                    raise ValueError("Price must be a positive number.")
            except ValueError as ve:
                print(f"Invalid price. Please enter a valid positive number for the price.\nError: {ve}")
                time.sleep(1)
                continue

            # Simulate a progress bar
            progress_bar(10, 'Adding item', 30)
            expenses.append([add_item, add_value])
            print(f"\n\nItem '{add_item.capitalize()} - {add_value}{currency} ' added successfully!", end="\n\n")
            break

    elif user_chosen_action == 'view':
        clear_term()  # Clear the terminal before each action
        print(f"\n===============|Viewing Expense list|===============")
        time.sleep(1)
        if not expenses:
            print("\nNo expenses added yet.")
            time.sleep(1)
        else:
            print("\n")
            print("_" * 50)
            print(f"{'Item no':<8} {'Item':<20} {'Price':>10}")
            print("_" * 50)
            for index, (item, price) in enumerate(expenses, start=1):
                print(f"{index:<8} {item:<20} {price:>10.2f} {currency}")
            print("_" * 50)
            print("\n\n")
            time.sleep(1)

    elif user_chosen_action == 'view excel':
        clear_term()  # Clear the terminal before each action
        print(f"\n===============|Viewing Expense list from Excel|===============")
        time.sleep(1)

        # Check if the Excel file exists
        if exists(excel_file):
            df = pd.read_excel(excel_file)  # Read the Excel file into a DataFrame

            # Ensure all column names are strings
            df.columns = df.columns.astype(str).str.strip().str.lower()  # Normalize column names
            print(f"Columns in Excel file: {df.columns}")  # Check column names

            if df.empty:
                print("\nThe Excel file is empty.")
            else:
                print("\n")
                print("_" * 50)
                print(f"{'Item no':<8} {'Item':<20} {'Price':>10}")
                print("_" * 50)
                for index, row in df.iterrows():
                    # Access columns with normalized names
                    print(f"{int(index) + 1:<8} {row['item']:<20} {row['price']:>10.2f} {currency}")
                print("_" * 50)
                print("\n\n")
        else:
            print("\nNo saved expenses found. Please add expenses first.")

        time.sleep(1)

    elif user_chosen_action == 'total':
        clear_term()  # Clear the terminal before each action
        print(f"\n===============|Viewing Total Expenses|===============")
        time.sleep(1)
        total = sum(price for _, price in expenses)
        # Simulate progress bar
        print("\n\n")
        progress_bar(10, 'Calculating total', 30)
        time.sleep(1)
        print("\n\n")
        print("_" * 50)
        print(f"{'Total':<20}{'Price':>10}")
        print("_" * 50)
        print(f"{'Total Expense':<20} {total:>10.2f}{currency}")
        print("_" * 50)
        print("\n\n")
        time.sleep(1)

    elif user_chosen_action == 'total excel':
        clear_term()  # Clear the terminal before each action
        print(f"\n===============|Total Expenses from Excel|===============")
        time.sleep(1)

        # Check if the Excel file exists
        if exists(excel_file):
            df = pd.read_excel(excel_file)  # Read the Excel file into a DataFrame

            # Ensure all column names are strings
            df.columns = df.columns.astype(str).str.strip().str.lower()  # Normalize column names

            if df.empty:
                print("\nThe Excel file is empty.")
            else:
                total = df['price'].sum()  # Calculate total from the 'price' column
                # Simulate progress bar
                print("\n\n")
                progress_bar(10, 'Calculating total from Excel', 30)
                time.sleep(1)
                print("\n\n")
                print("_" * 50)
                print(f"{'Total from Excel':<20}{'Price':>10}")
                print("_" * 50)
                print(f"{'Total Expense from Excel':<20} {total:>10.2f}{currency}")
                print("_" * 50)
                print("\n\n")
        else:
            print("\nNo saved expenses found. Please add expenses first.")

        time.sleep(1)

    elif user_chosen_action == 'exit':
        clear_term()  # Clear the terminal before each action
        print(f"\n===============|Closing the Expense Tracker|===============")
        time.sleep(1)
        print("\n\n")

        # Save the expenses to an Excel file when exiting
        df = pd.DataFrame(expenses, columns=['Item', 'Price'])
        df.to_excel(excel_file, index=False)  # Save the DataFrame to an Excel file
        print(f"Expenses saved to '{excel_file}'.")

        print("Goodbye!")
        print("\n\n")
        break
    else:
        print("Invalid action. Please choose from the list.")
        time.sleep(1)
