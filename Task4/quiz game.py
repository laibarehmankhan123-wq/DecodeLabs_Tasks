score = 0
total_questions = 3
 
print("=" * 40)
print("   WELCOME TO THE GENERAL KNOWLEDGE QUIZ")
print("=" * 40)
print(f"Answer {total_questions} questions. +1 point for every correct answer.\n")
 
# Step 1: Ask & Capture
raw_answer_1 = input("Q1. What is the capital of France? ")

answer_1 = raw_answer_1.strip().lower()

if answer_1 == "paris":
    score += 1
    print("Correct!\n")
else:
    print("Incorrect. The correct answer was Paris\n")
 
raw_answer_2 = input("Q2. Which planet is known as the Red Planet? ")
answer_2 = raw_answer_2.strip().lower()
if answer_2 == "mars":
    score += 1
    print("Correct!\n")
else:
    print("Incorrect. The correct answer was Mars. \n")
 
raw_answer_3 = input("Q3. Who wrote the play 'Romeo and Juliet'? ")
answer_3 = raw_answer_3.strip().lower()
if answer_3 == "william shakespeare" or answer_3 == "shakespeare":
    score += 1
    print("Correct! \n")
else:
    print("Incorrect. The correct answer was William Shakespeare. \n")
 
print("=" * 40)
print(f"QUIZ COMPLETE! Your final score is: {score:>2} / {total_questions}")
print("=" * 40)
 
if score == total_questions:
    print("Perfect score! You're a trivia master! ")
elif score >= 1:
    print("Good effort! Keep practicing to improve your score. ")
else:
    print("Better luck next time! Review the topics and try again")
 