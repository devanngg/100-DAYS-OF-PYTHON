import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
lives = 6

print(chosen_word)  # For testing
print("Current Lives:", lives)

# Create placeholder
word_length = len(chosen_word)
display = "_" * word_length
print(display)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Build new display
    new_display = ""
    for letter in chosen_word:
        if letter == guess:
            new_display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display
    print(display)

    # If guess not in chosen word → lose a life
    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess. Lives left:", lives)
        if lives == 0:
            game_over = True
            print("You lose!")

    # If no underscores left → player wins
    if "_" not in display:
        game_over = True
        print("You win!")
