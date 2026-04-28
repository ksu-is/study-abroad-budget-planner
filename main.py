# Study Abroad Budget Planner
# Author: Nevaeh Walker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: $"))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    if not expenses:
        print("No expenses added yet.")
    else:
        print("\nYour Expenses:")
        for expense in expenses:
            print(f"{expense['name']} - ${expense['amount']:.2f} - {expense['category']}")

def main():
    while True:
        print("\nStudy Abroad Budget Planner")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total spending")
        print("4. Exit")
        print("5. Exit")

       choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total_spending()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def view_total_spending():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ${total:.2f}")
main()
