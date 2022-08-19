import random
import os

from lib.hangman_art import logo, stages
from lib.hangman_words import word_list

##
# Clear the console and repaint with logo, lives left and a message
##
def clear_console(lives, message, wins, losses):
    # https://stackoverflow.com/a/2084628/4658283
    os.system("cls" if os.name == "nt" else "clear")

    print(logo)
    print(f"\nWins - {wins}\t Losses - {losses}")
    print(stages[lives])
    print(message)

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")


wins = 0
losses = 0

while True:
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    message = "Go ahead! Take your best guess."

    while not end_of_game:
        clear_console(lives, message, wins, losses)

        # Debug
        # print(f"Pssst, the solution is {chosen_word}.")

        guess = input("Guess a letter: ").lower()

        if guess in display:
            message = f"You've already guessed {guess}"
            continue

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            message = f"You guessed {guess}, that's not in the word. You lose a life."
            lives -= 1
            if lives == 0:
                end_of_game = True
                losses += 1
                clear_console(lives, message, wins, losses)
                print(f"You lose. The word was {chosen_word}.")
        else:
            message = f"You guessed the letter right."

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            wins += 1
            clear_console(lives, message, wins, losses)
            print("You win.")

    play_more = input("Do you want to play again? (Y/N): ")
    # Exit if the player does not want to continue
    if not play_more.lower() == "y":
        break
