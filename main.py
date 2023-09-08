
print("Welcome to the Quiz time!")


score = 0


print("\nQuestion 1: What is the capital of France?")
answer1 = input("A) Berlin\nB) Paris\nC) London\nYour answer (A/B/C): ")

if answer1.lower() == "b":
    print("Correct! Paris is the capital of France.")
    score += 1
else:
    print("Incorrect. The correct answer is B) Paris.")


print("\nQuestion 2: Which planet is known as the Red Planet?")
answer2 = input("A) Venus\nB) Mars\nC) Jupiter\nYour answer (A/B/C): ")

if answer2.lower() == "b":
    print("Correct! Mars is the Red Planet.")
    score += 1
else:
    print("Incorrect. The correct answer is B) Mars.")


print("\nQuestion 3: How many continents are there on Earth?")
answer3 = input("A) 5\nB) 6\nC) 7\nYour answer (A/B/C): ")

if answer3.lower() == "c":
    print("Correct! There are 7 continents on Earth.")
    score += 1
else:
    print("Incorrect. The correct answer is C) 7.")


print("\nThank you for taking the quiz!")
print(f"Your final score is {score} out of 3.")


if score == 3:
    print("Congratulations! You got all the questions right.")
elif score >= 1:
    print("Good job! You answered some questions correctly.")
else:
    print("Better luck next time. You didn't answer any questions correctly.")
