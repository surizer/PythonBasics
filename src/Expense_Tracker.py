expenses =[]
currency = 'kr'
while True:
    print(f"Welcome to the Expense Tracker!")
    user_available_action = ['add', 'view', 'total', 'exit']
    user_chosen_action = input(f"Choose an action {user_available_action}: ").lower()

    if user_chosen_action == 'add':
        user_input = input("Add an item and its price (coffee 10): ").split()
        if len(user_input) != 2:
            print("Invalid input. Please provide both item name and price.")
            continue
        add_item = user_input[0]
        try:
            add_value=float(user_input[1])
        except ValueError:
            print("Invalid price. Please enter a valid number for the price.")
            continue
        expenses.append([add_item, add_value])
        print(f"Item '{add_item} - {add_value}{currency} ' added successfully!")
    elif user_chosen_action == 'view':
        if not expenses:
            print("No expenses added yet")
        else:
            for index, (item, price) in enumerate(expenses, start=1):
                print(f"{index}. {item}: {price:.2f} {currency}")
    elif user_chosen_action == 'total':
        total = 0
        for _, price in expenses:
            total += price
        print(f"The total expense is {total:.2f}{currency}")
    elif user_chosen_action == 'exit':
        print("Goodbye!")
        break
    else:
        print("Invalid action. Please choose from the list")



