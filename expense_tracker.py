expenses = []
categories = {}

budget = float(input("Enter your monthly budget (Rs.): "))
while True:
    print("\n===== ExpenseIQ =====")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. View Analytics")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: ₹"))
        category = input(
            "Enter category (Food/Travel/Shopping/Education/Others): "
        )

        expenses.append(amount)

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

        print("Expense added successfully!")

    elif choice == "2":
        total = sum(expenses)

        print("\n----- Expense Summary -----")
        print(f"Total Expenses: Rs.{total}")
        print("\nCategory-wise Expenses:")
        for cat, amt in categories.items():
            print(f"{cat}: ₹{amt}")

        remaining = budget - total
        print(f"\nRemaining Budget: ₹{remaining}")

        if remaining < 0:
            print("⚠ Budget Exceeded!")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            total = sum(expenses)
            average = total / len(expenses)
            highest = max(expenses)
            lowest = min(expenses)

            print("\n----- Analytics -----")
            print(f"Total Expense: ₹{total}")
            print(f"Average Expense: ₹{average:.2f}")
            print(f"Highest Expense: ₹{highest}")
            print(f"Lowest Expense: ₹{lowest}")

            food_expense = categories.get("Food", 0)

            if food_expense > 3000:
                print(
                    "\nSuggestion: Your food expenses are high."
                )
                print(
                    "Try reducing food spending by 10%."
                )

    elif choice == "4":
        print("Thank you for using ExpenseIQ!")
        break

    else:
        print("Invalid Choice!")