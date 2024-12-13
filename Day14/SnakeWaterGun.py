# Snake Water Gun
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.


import random

# Tuple containing emojis
emoji_tuple = ("🔫", "🐍", "💧")

# Print instructions for the player
print(f"Enter 0 for Gun {emoji_tuple[0]}, 1 for Snake {emoji_tuple[1]}, and 2 for Water {emoji_tuple[2]}")

# Initialize variables
your_point = 0
comp_point = 0

# Game loop
while True:
    comp_choice = random.choice(emoji_tuple)  # Computer's random choice
    try:
        # Take player's input
        your_choice = int(input("Enter your option (0, 1, or 2): "))
        if your_choice not in [0, 1, 2]:
            print("Invalid input. Please choose 0, 1, or 2.")
            continue
    except ValueError:
        print("Please enter a valid number (0, 1, or 2).")
        continue

    # Display choices
    print(f"You {emoji_tuple[your_choice]} VS Computer {comp_choice}")

    # Check outcomes
    if emoji_tuple[your_choice] == comp_choice:
        print("Match Draw!")
    elif (
        (emoji_tuple[your_choice] == "🔫" and comp_choice == "🐍") or
        (emoji_tuple[your_choice] == "🐍" and comp_choice == "💧") or
        (emoji_tuple[your_choice] == "💧" and comp_choice == "🔫")
    ):
        print("You Win!")
        your_point += 1
    else:
        print("Computer Wins!")
        comp_point += 1

    # Show scores
    print(f"Score -> You: {your_point}, Computer: {comp_point}")

    # Ask if the player wants to continue
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thank you for playing!")
        break




