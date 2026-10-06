expenses = []

def add_expense():
    item = input("Enter item: ")
    price = float(input("Enter price: "))

    expenses.append({
        "item": item,
        "price": price
    })

    print("Expense added successfully!")


def show_expenses():
    if not expenses:
        print("No expenses stored.")
        return

    print("\n--- Stored Expenses ---")

    for expense in expenses:
        print("Item:", expense["item"])
        print("Price:", expense["price"])
        print("----------------")

print("==--- Expense  Traker ---==")
while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
        print("==-=-=-=-=-=-=-=-=-=-=-==")

    elif choice == "2":
        show_expenses()
        print("==-=-=-=-=-=-=-=-=-=-=-==")
      
    elif choice == "3":
        total = sum(expense["price"] for expense in expenses)
        print("Total Expense:", total)
        print("==-=-=-=-=-=-=-=-=-=-=-==")

    elif choice == "4":
        print("^^^^^|||Thanks for using our Expense Traker|||^^^^^ !")
        print("==-=-=-=-=-=-=-=-=-=-=-==")
        
        break
        
    

    else:
        print("Invalid choice.")