# General Knowledge Quiz

A simple command-line General Knowledge Quiz developed in Python. This project allows users to answer multiple-choice style questions (using text input), checks their answers, and displays a final score at the end of the quiz.

## Features

- Interactive command-line interface
- Three general knowledge questions
- Input sanitization using `.strip()` and `.lower()`
- Automatic score calculation
- Instant feedback after each question
- Final performance message based on the user's score

## Technologies Used

- Python 3

## Concepts Demonstrated

- Variables
- User Input (`input()`)
- String Methods (`strip()`, `lower()`)
- Conditional Statements (`if`, `elif`, `else`)
- Score Tracking
- Formatted Output using f-strings

## Project Structure

```
General-Knowledge-Quiz/
│── quiz.py
└── README.md
```

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python quiz.py
```

## Example Output

```
========================================
WELCOME TO THE GENERAL KNOWLEDGE QUIZ
========================================

Q1. What is the capital of France?
> Paris

Correct!

Q2. Which planet is known as the Red Planet?
> Mars

Correct!

Q3. Who wrote the play 'Romeo and Juliet'?
> Shakespeare

Correct!

========================================
QUIZ COMPLETE! Your final score is: 3/3
========================================

Perfect score! You're a trivia master!
```

## Learning Outcomes

This project demonstrates fundamental Python programming concepts, including user interaction, input validation, decision-making with conditional statements, score management, and formatted console output.

## Author

**Laiba Rehman**