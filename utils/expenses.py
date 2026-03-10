from config.db import get_connection, close_connection
#CRUD FUNCTIONS

def get_all_expenses():
    connection = get_connection()
    #Defensive line
    if not connection:
        return []
    #create a cursor
    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        print("Expenses fetched successfully")
        return expenses
    
    except Exception as e:
        print(f"Failed to fetch expenses{e}") 
        return []
    
    finally:
        close_connection(connection, cursor)


def get_expenses_by_id(expense_id):
    connection = get_connection()
    if not connection:
        return None
    

    cursor = connection.cursor(dictionary=True, buffered=True)

    try:
        cursor.execute("SELECT * FROM expenses WHERE expense_id =%s",(expense_id,))
        expense = cursor.fetchone()
        print("Expense fectched successfully")
        return expense
    
    except Exception as e:
        print(f"Failed to fetch expenses{e}") 
        return None
    
    finally:
        close_connection(connection, cursor)


def create_expense(amount, category, description):
    connection = get_connection()
    if not connection:
        return False

    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO expenses (amount, category, description) VALUES (%s,%s,%s)",
                        (amount, category, description))
        connection.commit()
        print("Expense created successfully") 
        return True

    except Exception as e:
        print(f"Failed to create expense{e}")
        return False
    
    finally:
        close_connection(connection, cursor)
        

def update_expenses(expense_id, ampount, category, description):
    connection = get_connection()
    if not connection:
        return False
    
    cursor = connection.cursor()

    try:       
        cursor.execute("""
            UPDATE expenses SET
            amount =%s,
            category=%s,
            description=%s
            WHERE expense_id =%s
        """,(ampount, category, description,expense_id))
        
        connection.commit()
        print(f"Expense {expense_id} updated successfully")
        return True
    
    except Exception as e:
        print(f"Failed updating expense{e}")
        return False
    
    finally:
        close_connection(connection, cursor)

def delete_expense(expense_id):
    connection = get_connection()
    if not connection:
        return False

    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM expenses WHERE expense_id =%s",
                        (expense_id,))
        
        connection.commit()

        if cursor.rowcount == 0:
            print(f"❌ Expense {expense_id} not found.")
            return False

        print(f"Expense {expense_id} deleted successfully")
        return True
    
    except Exception as e:
        print(f"Failed deleting expense{e}")
        return False
    
    finally:
        close_connection(connection, cursor)
