#Radney Johnson
#LLM_LAB1
#12/06/2025
#Simple 3-question quiz

score = 0

print("Welcome to the Quiz!\n")

# Question 1
q1 = input("1. What is the capital of France? ")
if q1.strip().lower() == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect.\n")

# Question 2
q2 = input("2. What is 5 + 7? ")
if q2.strip() == "12":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect.\n")

# Question 3
q3 = input("3. What programming language is this quiz written in? ")
if q3.strip().lower() == "python":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect.\n")

print(f"Quiz complete! Your score: {score}/3")
