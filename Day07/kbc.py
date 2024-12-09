# List of questions for the quiz
kbc_questions = (
    "Who was the first woman to receive the Bharat Ratna?",
    "Which planet is known as the 'Red Planet'?",
    "In which year did India win its first Cricket World Cup?",
    "Which is the longest river in the world?",
    "Who wrote the book 'The Discovery of India'?",
    "What is the capital of Australia?",
    "Which metal is primarily used in the production of stainless steel?"
)

# Correct answers corresponding to each question
correct_answers = (
    "Mother Teresa",  # Answer for question 1
    "Mars",           # Answer for question 2
    "1983",           # Answer for question 3
    "Nile",           # Answer for question 4
    "Jawaharlal Nehru", # Answer for question 5
    "Canberra",       # Answer for question 6
    "Chromium"        # Answer for question 7
)

# Prize amounts for each question
prize_amounts = (
    1000,       # Prize for question 1
    5000,       # Prize for question 2
    10000,      # Prize for question 3
    320000,     # Prize for question 4
    640000,     # Prize for question 5
    1250000,    # Prize for question 6
    70000000    # Prize for question 7 (₹7 crore)
)

# Options for each question
options = [
    ["Mother Teresa", "Indira Gandhi", "Sarojini Naidu", "Savitribai Phule"],  # Options for question 1
    ["Mars", "Jupiter", "Venus", "Mercury"],                                  # Options for question 2
    ["1981", "1983", "1985", "1987"],                                         # Options for question 3
    ["Amazon", "Yangtze", "Nile", "Mississippi"],                             # Options for question 4
    ["Mahatma Gandhi", "Subhas Chandra Bose", "Rabindranath Tagore", "Jawaharlal Nehru"],  # Options for question 5
    ["Sydney", "Melbourne", "Canberra", "Perth"],                             # Options for question 6
    ["Copper", "Chromium", "Aluminum", "Nickel"]                              # Options for question 7
]

# Initialize variables for tracking progress and total prize money
count = 0  # Keeps track of the current question number
amount = 0  # Keeps track of the total prize money won

# Start the game loop
while count < len(kbc_questions):  # Loop until all questions are asked or a wrong answer is given
    # Print the current question
    print(f"\n\nQuestion {count + 1}: {kbc_questions[count]} ")
    
    # Print the options for the current question
    for option in options[count]:
        print(f"- {option}")
    print()  # Add a blank line for better readability

    # Ask the user for their answer
    answer = input("Enter the correct answer: ").title()  # Converts the input to title case for comparison

    # Check if the user's answer is correct
    if answer == correct_answers[count]:
        # If correct, add the prize amount for this question to the total
        amount += prize_amounts[count]
        print("Your answer is correct!")
        print(f"Your total winnings: ₹{amount}")
    else:
        # If wrong, end the game and show the correct answer and total winnings
        print("Oops! Wrong answer.")
        print(f"Correct answer is {correct_answers[count]}")
        print(f"You win ₹{amount}.")
        break  # Exit the loop

    # Move to the next question
    count += 1

# End of game
if count == len(kbc_questions):
    print(f"Congratulations! You've answered all questions correctly and won ₹{amount}.")
