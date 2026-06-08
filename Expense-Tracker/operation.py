from datetime import date
time = date.today()


import os

print(os.path.abspath("expenses.txt"))

def get_next_id():
    try:
        with open("fullstack-internship-bidit/Expense-Tracker/expenses.txt", "r") as file:
            students = file.readlines()

            if not students:
                return 1

            last_student = students[-1].strip()
            last_id = int(last_student.split(",")[0])

            return last_id + 1

    except FileNotFoundError:
        return 1
    

def add_expense():
    with open("fullstack-internship-bidit/Expense-Tracker/expenses.txt", "a") as file:
        id = get_next_id()
        time = date.today()
        amount = float(input("Enter cost: "))
        description = input("What was that expense: ")
        file.write(f"{id}, {time}, {description}, {amount}\n")

    print("Expense tracker updated successfully")


def display_expense():
    with open("fullstack-internship-bidit/Expense-Tracker/expenses.txt", "r") as file:
        for line in file:
            proper = line.strip()
            print(proper)

def total_all():
    total = 0
    with open("fullstack-internship-bidit/Expense-Tracker/expenses.txt", "r") as file:
        for line in file:
            val = line.strip().split(',')
            
            if len(val)>3:
                cost = float(val[3])
                total = total + cost
    
    print(f"The total cost is : Rs.{total:.2f}")


def delete_expense():
    with open("fullstack-internship-bidit/Expense-tracker/expenses.txt", "r") as file:
        expenses = file.readlines()

    display_expense()

    choice = int(input("Enter expense number to delete: "))

    if 1 <= choice <= len(expenses):

        print("\nSelected Expense:")
        print(expenses[choice - 1])

        confirm = input("Are you sure? (y/n): ").lower()

        if confirm == "y":
            expenses.pop(choice - 1)

            with open("fullstack-internship-bidit/expense-tracker/expenses.txt", "w") as file:
                file.writelines(expenses)

            print("Expense deleted successfully.")
        else:
            print("Deletion cancelled.")

    else:
        print("Invalid expense number.")


def monthly_tracker():
    month =  input("Enter month (MM): ")
    total = 0
    with open("fullstack-internship-bidit/Expense-tracker/expenses.txt", "r") as file:
        for expenses in file:
            parts = expenses.strip().split(',')

            date = parts[1]
            cost = float(parts[3])

            expenses_month = date.split("-")[1]

            if expenses_month == month:
                total +=cost

    print(f"The total cost for month {month} is {total}")