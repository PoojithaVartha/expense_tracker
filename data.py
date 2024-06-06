from datetime import datetime

class Expense:
  """Represents an expense with amount, category, and date."""
  def __init__(self, amount, category, date=datetime.today()):
    self.amount = amount
    self.category = category
    self.date = date

def get_float(prompt):
  """Gets a floating-point number from the user."""
  while True:
    try:
      value = float(input(prompt))
      return value
    except ValueError:
      print("Invalid input. Please enter a number.")

def get_category():
  """Gets the expense category from the user."""
  categories = ["Food", "Bills", "Entertainment", "Other"]
  print("Expense Categories:")
  for i, category in enumerate(categories):
    print(f"{i+1}. {category}")
  while True:
    try:
      choice = int(input("Enter the number of your expense category (or 0 to exit): "))
      if 0 <= choice <= len(categories):
        return categories[choice-1] if choice > 0 else None
      else:
        print("Invalid choice. Please enter a number between 0 and", len(categories))
    except ValueError:
      print("Invalid input. Please enter a number.")

def add_expense(expenses):
  """Adds a new expense to the expense list."""
  amount = get_float("Enter the amount of the expense: $")
  category = get_category()
  if category:
    expenses.append(Expense(amount, category))
    print(f"Expense of ${amount:.2f} added to category: {category}")
  else:
    print("Expense added without a category.")

def view_expenses(expenses):
  """Prints the current list of expenses."""
  if not expenses:
    print("There are no expenses to display.")
    return
  print("\nYour Expenses:")
  for i, expense in enumerate(expenses):
    print(f"{i+1}. ${expense.amount:.2f} ({expense.category}) on {expense.date.strftime('%Y-%m-%d')}")

def edit_expense(expenses):
  """Edits an existing expense."""
  view_expenses(expenses)
  if not expenses:
    return
  while True:
    try:
      index = int(input("Enter the number of the expense to edit (or 0 to exit): "))
      if 0 < index <= len(expenses):
        expense = expenses[index - 1]
        new_amount = get_float("Enter the new amount (or press Enter to keep the current amount): ")
        if new_amount != "":
          expense.amount = new_amount
        new_category = get_category()
        if new_category:
          expense.category = new_category
        print("Expense edited successfully.")
        return
      elif index == 0:
        return
      else:
        print("Invalid choice. Please enter a number between 0 and", len(expenses))
    except ValueError:
      print("Invalid input. Please enter a number.")

def delete_expense(expenses):
  """Deletes an existing expense."""
  view_expenses(expenses)
  if not expenses:
    return
  while True:
    try:
      index = int(input("Enter the number of the expense to delete (or 0 to exit): "))
      if 0 < index <= len(expenses):
        del expenses[index - 1]
        print("Expense deleted successfully.")
        return
      elif index == 0:
        return
      else:
        print("Invalid choice. Please enter a number between 0 and", len(expenses))
    except ValueError:
      print("Invalid input. Please enter a number.")

def main():
  """Main loop for the expense tracker."""
  expenses = []  # List to store expenses
  while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
      add_expense(expenses)
    elif choice == '2':
      view_expenses(expenses)
    elif choice == '3':
      edit_expense(expenses)
    elif choice == '4':
