import random
from random import choice
from os import system, name  # To clear the screen

from game_data import data
from art import logo
from art import vs


# Function to clear the screen
def clear_screen():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac and Linux
    else:
        _ = system('clear')


def choices(account_b=None):
    # If account_b is provided, make it the new choice_A
    choice_A = account_b if account_b else random.choice(data)
    choice_B = random.choice(data)
    # Ensure choice_A and choice_B are not the same
    while choice_A == choice_B:
        choice_B = random.choice(data)

    count_A = choice_A['follower_count']
    count_B = choice_B['follower_count']
    print(logo)
    print(f"Choice A is : {choice_A['name']}, {choice_A['description']}, {choice_A['country']}")
    print(vs)
    print(f"Choice B is : {choice_B['name']}, {choice_B['description']}, {choice_B['country']}")

    return choice_A, choice_B, count_A, count_B


def play_game():
    game_over = False
    guess_count = 0
    lives = 3  # Start with 3 lives
    account_b = None  # Initialize for seamless transition

    while not game_over:
        clear_screen()  # Clear the screen before each round

        # Use the previous "B" as the new "A" for the next round
        choice_A, choice_B, count_A, count_B = choices(account_b)

        try:
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            print(f"You have {lives} lives")
            while guess not in ["a", "b"]:
                guess = input("Invalid input. Please type 'A' or 'B': ").lower()
        except ValueError:
            break

        difference = abs(count_A - count_B)

        # Compare follower counts based on the player's guess
        if guess == "a" and count_A > count_B:
            guess_count += 1  # Increment score
            print(f"Correct! Choice A has {difference} million more followers than Choice B.")
            print(f"Correct! Your score is {guess_count}")
            account_b = choice_A  # Make choice_A the next round's choice_B
        elif guess == "b" and count_B > count_A:
            guess_count += 1  # Increment score
            print(f"Correct! Choice B has {difference} million more followers than Choice A.")
            print(f"Correct! Your score is {guess_count}")
            account_b = choice_B  # Make choice_B the next round's choice_A
        else:
            lives -= 1  # Lose a life
            if lives > 0:
                print(f"Wrong! You have {lives} lives left.")
                account_b = None  # Reset for the next round
            else:
                print(f"Game Over homie. Your final score: {guess_count}")
                lives = 3  # Reset lives for next game
                guess_count = 0  # Reset score for next game
                account_b = None  # Reset account for fresh start
                print("Restarting the game automatically...")
                clear_screen()  # Clear the screen for a fresh start

        # No need for a manual reset — game restarts automatically when lives reach 0


# Start the game
play_game()