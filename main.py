from utils.expenses import create_expense, get_all_expenses,get_expenses_by_id,delete_expense

while True:
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expense by ID")
    print("4. Delete Expense")
    print("5. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        #Add expenses
        amount = float(input(("Enter amount: ")))
        category = input("Enter expensse category: ")
        description = input("Enter expense description: ")
        create_expense(amount, category, description)
        print("\n")
    
    elif choice == "2":
        #view all expenses
        expenses = get_all_expenses()
        print(f"\nAll expenses({len(expenses)} found):")
        for expense in expenses:
            print(f"{expense['expense_id']} - {expense['amount']} - {expense['category']} - {expense['description']}\n")
            
    elif choice =="3":
        #View expense by Id
        expense_id = int(input("Enter the expense_id: "))
        
        expense = get_expenses_by_id(expense_id)
        if expense:
            print(f"{expense_id}- {expense['amount']} - {expense['category']} - {expense['description']}\n")
        else:
            print(f"Expense ID- {expense_id} cannot be found")

    elif choice == "4":
        expense_id = int(input("Enter expense_id: "))
        expense = delete_expense(expense_id)


    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid input(Enter from(1-5))")    