import datetime

expenses = []

def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (e.g., food, entertainment, bills): ").strip()
        date = datetime.date.today()  
        
        expense = { 
                   
            "amount": amount,
            "category": category,
            "date": date
        }
        expenses.append(expense)
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_expenses():
    if expenses:
        print("\nAll Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. Amount: {expense['amount']} | Category: {expense['category']} | Date: {expense['date']}")
        print()
    else:
        print("No expenses recorded.\n")

def view_total_by_category():
    category_totals = {}
    
    for expense in expenses:
        category = expense["category"]
        category_totals[category] = category_totals.get(category, 0) + expense["amount"]
    
    print("\nTotal Expenses by Category:")
    for category, total in category_totals.items():
        print(f"{category}: {total:.2f}Rs")
    print()

def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total by Category")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_total_by_category()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


main()