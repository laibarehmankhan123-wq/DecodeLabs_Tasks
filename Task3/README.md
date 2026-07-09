# Random Password Generator

A secure and user-friendly **Random Password Generator** built with Python. This project generates random passwords based on a user-defined length and provides an estimate of password strength using entropy calculations.

Developed as **Project 3** of the DecodeLabs Python Programming Industrial Training Kit, this project demonstrates module integration, string manipulation, user input validation, and random password generation.

---

## Features

* Generate random passwords of a user-defined length
* Optional inclusion of special characters
* Uses Python's `random` and `string` modules
* Validates user input
* Calculates password entropy
* Displays password strength rating
* Clean, modular, and beginner-friendly code

---

## Concepts Practiced

* Python Functions
* Loops
* Conditional Statements
* Input Validation
* Module Importing
* String Manipulation
* Random Password Generation
* Password Entropy Calculation

---

## 🛠 Technologies Used

* Python 3
* `random`
* `string`
* `math`

---

## Project Structure

```text
Random Password Generator/
│
├── Random_password_generator.py
└── README.md
```

---

## How to Run
* Make sure Python 3 is installed.
* Open a terminal in the project folder.
* Run:
python Random_password_generator.py
or
python3 Random_password_generator.py


---

## Example Output

```text
=======================================================
Random Password Generator
=======================================================

Enter desired password length (e.g., 16): 16
Include special symbols (@, #, $, etc.)? (y/n): y

--- Generated Password ---

A@7mQ#9xLp2!Rw5Z

Length: 16 characters
Character pool size: 94
Entropy: 104.88 bits
Strength rating: Very Strong
=======================================================
```

---

## Password Strength

The application estimates password strength using the entropy formula:

**Entropy = Password Length × log₂(Character Pool Size)**

Based on the calculated entropy, each password is classified as:

* Weak
* Moderate
* Strong
* Very Strong

This provides users with a simple indication of how resistant a password is to brute-force attacks.

---

## Learning Outcomes

Through this project, I gained practical experience with:

* Using Python's built-in modules
* Generating random passwords
* Validating user input
* Working with strings and lists
* Writing modular and reusable code
* Applying basic password security concepts
* Calculating password entropy

---

## License

This project was developed for educational purposes as part of the DecodeLabs Python Programming Industrial Training Program.
