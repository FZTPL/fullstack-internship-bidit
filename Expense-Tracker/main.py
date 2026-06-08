from operation import *
while True:
    choice = int(input("""

1. Add Expense
2. List Expenses
3. Total Expense
4. Delete Expense
5. Monthly Tracker
6. Exit
                    
Enter your choice: """))

    match choice:
        case 1:
            add_expense()
        
        case 2:
            display_expense()

        case 3:
            total_all()

        case 4:
            delete_expense()

        case 5:
            monthly_tracker()  
             
        case 6:
            break

        case _:
            print("Invalid choice")