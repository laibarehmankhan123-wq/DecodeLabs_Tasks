# Expense Tracker

A simple command-line Expense Tracker built with Python. This project allows users to enter multiple expenses, keeps a running total, validates user input, and displays the total amount spent at the end of the session.

---

## Project Overview

This Expense Tracker was developed as **Project 2** for the DecodeLabs Python Programming Industrial Training Kit.

The main objective of this project is to demonstrate the use of:

- Variables
- User Input
- While Loops
- Conditional Statements
- Exception Handling
- Mathematical Operations
- Accumulator Pattern

---

## Features

- Enter multiple expenses
- Running total after each valid expense
- Rejects invalid (non-numeric) input
- Rejects negative expense values
- Exit anytime by typing `done`
- Displays a formatted expense summary

---

## Technologies Used

- Python 3

---

## Project Structure

```
Expense Tracker/
│
├── EXPENSE_TRACKER.py
└── README.md
```

---

## How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run:

```bash
python EXPENSE_TRACKER.py
```

or

```bash
python3 EXPENSE_TRACKER.py
```

---

## Example

```
Enter an expense (or 'done' to finish): 100
Current total expenses: $100.00

Enter an expense (or 'done' to finish): 50
Current total expenses: $150.00

Enter an expense (or 'done' to finish): done

======================
EXPENSE SUMMARY
======================
Total Spent: $150.00
Thank you for using the Expense Tracker!
```

---

## Learning Outcomes

Through this project, I practiced:

- Working with loops
- Input validation
- Exception handling using `try` and `except`
- Using accumulators to process data
- Building a simple interactive console application

---

## Author

**Laiba Rehman**

Project completed as part of the **DecodeLabs Python Programming Industrial Training Program (2026)**.