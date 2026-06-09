# ============================================================
# QUIZ GAME - Bro Code Python Tutorial Project
# ============================================================
# This is a simple quiz game that asks the user multiple-choice
# questions, checks their answers, and displays the final score.
# Concepts used: tuples, lists, for loops, if statements, 
# input validation, type casting, and f-strings.
# ============================================================

# --- QUESTIONS TUPLE ---
# A tuple containing all the quiz questions as strings.
# Tuples are ordered and unchangeable - perfect for a fixed set of questions.
questions = (
    "1. How many planets are there in the solar system?",
    "2. What is 7 + 4?",
    "3. What is the chemical symbol for water?",
    "4. Which animal is known as the 'King of the Jungle'?",
    "5. What is the capital of France?"
)

# --- OPTIONS TUPLE ---
# A tuple containing the multiple-choice options for each question.
# Each element is a string with all 4 options separated by commas.
options = (
    "A. 7     B. 8     C. 9     D. 10",
    "A. 10    B. 9     C. 12    D. 11",
    "A. CO2   B. H2O   C. NaCl  D. O2",
    "A. Tiger  B. Bear  C. Lion  D. Elephant",
    "A. London B. Berlin C. Madrid D. Paris"
)

# --- ANSWERS LIST ---
# A list containing the correct answer for each question.
# We use letters (A, B, C, D) mapped to numbers (1, 2, 3, 4).
# Index 0 = first question, index 1 = second question, etc.
answers = ("C", "D", "B", "C", "D")

# --- SCORE VARIABLE ---
# Keeps track of the number of correct answers.
# Starts at 0 and increments by 1 for each correct guess.
score = 0

# --- LIST TO STORE USER'S GUESSES ---
# This list will hold all the user's guesses for final summary display.
guesses = []

# --- WELCOME MESSAGE ---
# Display a title banner for the quiz game.
print("=" * 50)
print("          WELCOME TO THE QUIZ GAME!")
print("=" * 50)
print("Answer the following questions by typing A, B, C, or D.\n")

# --- MAIN GAME LOOP ---
# Loop through each question using its index.
# range(len(questions)) gives us indices 0 through 4 (for 5 questions).
for i in range(len(questions)):

    # Display the current question number and the question text.
    print("-" * 50)
    print(questions[i])
    print()
    
    # Display the multiple-choice options for the current question.
    print(options[i])
    print()

    # --- GET USER'S GUESS ---
    # Prompt the user to enter their answer.
    guess = input("Enter your answer (A/B/C/D): ").upper()

    # --- INPUT VALIDATION ---
    # Keep asking until the user enters a valid choice (A, B, C, or D).
    # The while loop checks if guess is NOT one of the valid options.
    while guess not in ("A", "B", "C", "D"):
        print("X Invalid choice! Please enter A, B, C, or D.")
        guess = input("Enter your answer (A/B/C/D): ").upper()

    # Store the validated guess in our guesses list for later use.
    guesses.append(guess)

    # --- CHECK ANSWER ---
    # Compare the user's guess with the correct answer from the answers tuple.
    if guess == answers[i]:
        # Correct! Increment the score and give positive feedback.
        score += 1
        print("Correct!")
    else:
        # Incorrect. Display the correct answer.
        print("Incorrect!")
        print(f"   The correct answer was: {answers[i]}")

    print()  # Blank line for spacing between questions.

# --- DISPLAY FINAL SCORE ---
# After all questions have been answered, show the final results.
print("=" * 50)
print("                    ***  RESULTS  ***")
print("=" * 50)
print()

# Display the score as a fraction (e.g., "You got 4/5 correct!").
print(f"You got {score} out of {len(questions)} correct!")

# Calculate and display the percentage score.
percentage = (score / len(questions)) * 100
print(f"That's {percentage:.1f}%!")

print()

# --- PERFORMANCE FEEDBACK ---
# Give the user a rating based on their score.
if score == len(questions):
    print("*** Perfect score! You're a genius! ***")
elif score >= len(questions) * 0.7:
    print("Great job! You really know your stuff!")
elif score >= len(questions) * 0.5:
    print("Not bad! Keep learning and you'll improve!")
else:
    print("Keep studying! You'll do better next time!")

print()
print("-" * 50)
print("--- SUMMARY OF YOUR ANSWERS ---")
print("-" * 50)

# --- ANSWER SUMMARY ---
# Loop through and show each question with the user's answer vs correct answer.
for i in range(len(questions)):
    # Display question number, user's guess, and the correct answer.
    # Show a checkmark if correct, X if wrong.
    status = "CORRECT" if guesses[i] == answers[i] else "WRONG"
    print(f"Q{i + 1}: You answered [{guesses[i]}] | Correct: [{answers[i]}] {status}")

print()
print("=" * 50)
print("        Thanks for playing the Quiz Game!")
print("=" * 50)
