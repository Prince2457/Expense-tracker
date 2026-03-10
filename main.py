from utils.expenses import create_expense, get_all_expenses

def main():
    print("💰 Expense Tracker")
    print("=" * 40)

    #Create a test expense
    create_expense(50.00, 'food', 'Bought lunch')
    create_expense(20.00, 'transport', 'Uber ride')

    #get all expense
    expenses = get_all_expenses()
    print(f"\nAll expense ({len(expenses)} found): ")

    for expense in expenses:
        print(f"{expense['expense_id']} - {expense['category']} - {expense['amount']}")


if __name__=="__main__":
    main()
