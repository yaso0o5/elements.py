import csv
from datetime import datetime
from pathlib import Path


CSV_FILE = Path("expenses.csv")
FIELDNAMES = ["amount", "category", "description", "date"]


def main():
    """Run the Expense Tracker menu."""
    print("Expense Tracker")
    print("----------------")

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(CSV_FILE)
        elif choice == "2":
            view_expenses(CSV_FILE)
        elif choice == "3":
            search_expenses_by_category(CSV_FILE)
        elif choice == "4":
            show_total_expenses(CSV_FILE)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 5.")


def display_menu():
    """Show the main menu choices."""
    print()
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Search expenses by category")
    print("4. Calculate total expenses")
    print("5. Exit")


def add_expense(file_path):
    """Ask the user for expense details and save the expense."""
    amount = get_amount()
    category = get_required_text("Category: ")
    description = get_required_text("Description: ")
    date = get_date()

    expense = {
        "amount": f"{amount:.2f}",
        "category": category,
        "description": description,
        "date": date,
    }

    try:
        save_expense(file_path, expense)
    except OSError:
        print("Sorry, the expense could not be saved.")
    else:
        print("Expense added successfully.")


def get_amount():
    """Get a positive amount from the user."""
    while True:
        amount = input("Amount: ").strip()

        try:
            amount = float(amount)
        except ValueError:
            print("Amount must be a number.")
            continue

        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        return amount


def get_required_text(prompt):
    """Get non-empty text from the user."""
    while True:
        text = input(prompt).strip()

        if text:
            return text

        print("This field cannot be empty.")


def get_date():
    """Get a valid date or use today's date if the user presses Enter."""
    while True:
        date = input("Date (YYYY-MM-DD, press Enter for today): ").strip()

        if not date:
                        return datetime.today().strftime("%Y-%m-%d")

        if is_valid_date(date):
            return date

        print("Date must be in YYYY-MM-DD format.")


def is_valid_date(date_text):
    """Return True if date_text is a real date in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        return False

    return True


def save_expense(file_path, expense):
    """Write one expense to the CSV file."""
    file_exists = Path(file_path).exists()

    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow(expense)


def load_expenses(file_path):
    """Read all expenses from the CSV file."""
    try:
        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []
    except OSError:
        print("Sorry, the expenses file could not be read.")
        return []


def view_expenses(file_path):
    """Display every saved expense."""
    expenses = load_expenses(file_path)

    if not expenses:
        print("No expenses found.")
        return

    print_expenses(expenses)


def search_expenses_by_category(file_path):
    """Display expenses that match a category entered by the user."""
    category = get_required_text("Category to search: ").lower()
    expenses = load_expenses(file_path)
    matches = filter_expenses_by_category(expenses, category)

    if not matches:
        print("No expenses found in that category.")
        return

    print_expenses(matches)


def filter_expenses_by_category(expenses, category):
    """Return expenses whose category matches the search term."""
    return [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]


def show_total_expenses(file_path):
    """Calculate and display the total of all expenses."""
    expenses = load_expenses(file_path)
    total = calculate_total(expenses)
    print(f"Total expenses: ${total:.2f}")


def calculate_total(expenses):
    """Return the total amount for a list of expenses."""
    total = 0

    for expense in expenses:
        try:
            total += float(expense["amount"])
        except (KeyError, ValueError):
            continue

    return total


def print_expenses(expenses):
    """Print expenses in a readable table."""
    print()
    print(f"{'Amount':>10}  {'Category':<15}  {'Date':<10}  Description")
    print("-" * 55)

    for expense in expenses:
        print(
            f"${float(expense['amount']):>9.2f}  "
            f"{expense['category']:<15}  "
            f"{expense['date']:<10}  "
            f"{expense['description']}"
        )


if __name__ == "__main__":
    main()