# ASCII art (optional) – you can replace with text if you don’t have them
rock = "✊"
paper = "✋"
scissors = "✌️"

# User input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_input == 0:
    print("You chose: Rock " + rock)
elif user_input == 1:
    print("You chose: Paper " + paper)
elif user_input == 2:
    print("You chose: Scissors " + scissors)
else:
    print("Invalid choice!")
    exit()

# Computer choice
import random
computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print("Computer chose: Rock " + rock)
elif computer_choice == 1:
    print("Computer chose: Paper " + paper)
elif computer_choice == 2:
    print("Computer chose: Scissors " + scissors)

# Game result logic
if computer_choice == user_input:
    print("It's a TIE!")
elif computer_choice == 0 and user_input == 1:
    print("You win! Paper covers Rock.")
elif computer_choice == 0 and user_input == 2:
    print("Computer wins! Rock crushes Scissors.")
elif computer_choice == 1 and user_input == 0:
    print("Computer wins! Paper covers Rock.")
elif computer_choice == 1 and user_input == 2:
    print("You win! Scissors cut Paper.")
elif computer_choice == 2 and user_input == 0:
    print("You win! Rock crushes Scissors.")
elif computer_choice == 2 and user_input == 1:
    print("Computer wins! Scissors cut Paper.")
