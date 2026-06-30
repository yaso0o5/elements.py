# elements.py
# Expense Tracker

Final project

# Expense Tracker

Final project for the Building AI course

## Summary

Expense Tracker is a terminal-based Python program designed to help users record and manage their daily spending in a simple way. The program allows users to add new expenses by entering an amount, category, description, and date. Each expense is saved in a CSV file, which means the data stays available even after the program is closed. This makes the project useful for students or anyone who wants to keep track of money without using a complicated finance application.
The program uses a menu-based interface where the user can choose from different options. The user can add a new expense, view all saved expenses, search expenses by category, calculate the total amount spent, or exit the program. Input validation is included to make sure the amount is a positive number and the date is valid. The program also handles errors gracefully, such as when the CSV file does not exist yet.
This project is organized using functions, which makes the code cleaner and easier to understand. For example, separate functions are used for adding expenses, loading expenses, saving data, searching by category, and calculating totals. The project also includes pytest test functions to check important parts of the program, such as date validation, category searching, and total calculation.
Overall, Expense Tracker is a beginner-friendly project that demonstrates important Python concepts, including functions, loops, conditionals, file handling, CSV files, input validation, error handling, and testing. It is a suitable final project because it solves a real-life problem using clear and organized Python code an thank you for making me do this and good bye.


## Background

Many people spend money every day but do not always remember where their money went. This can make it harder to plan a budget, avoid overspending, or understand spending habits. The problem is common for students, workers, and families because daily expenses can add up quickly.

Problems this project helps with:

* forgetting daily expenses
* losing track of spending categories
* not knowing the total amount spent
* needing a simple record without a complicated finance app

## How is it used?

The user runs the program in a terminal and chooses an option from a menu. The program asks the user to type the amount, category, description, and date of an expense.

Example:

```text
Expense Tracker
----------------

1. Add a new expense
2. View all expenses
3. Search expenses by category
4. Calculate total expenses
5. Exit
Choose an option: 1
Amount: 25
Category: clothes
Description: shirt
Date (YYYY-MM-DD, press Enter for today): 2026-06-19
Expense added successfully.