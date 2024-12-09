import random

from art import logo



def diff():
    while True:
        attempts = 0
        difficulty = input("Choose difficulty 'hard' or 'easy': ").lower()
        if difficulty == "hard":
            attempts = 5
            break
        elif difficulty == "easy":
            attempts = 10
            break
        else:
            print("Invalid input. Please enter 'hard' or 'easy'.")
    # print(f"You have {attempts} attempts remaining to guess the number.")
    return difficulty, attempts

def number():
    num = random.randint(1,100)
    return num
num = number()
difficulty, attempts = diff()
while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")

    try:
        guess = int(input("Make a guess: "))


        # Check if the guess is out of range
        if guess < 1 or guess > 100:
            print("Out of range! Please guess a number between 1 and 100.")
            continue  # No attempt is deducted, and the player guesses again
    except ValueError:
        print("Please enter a valid integer.")
        continue
    if guess == num:
        print("you win")
        break
    elif guess > num:
        print("too high")
        attempts -= 1
    else:
        print("too low")
        attempts -= 1
if attempts == 0:
    print("you lose homie")
    print(f"The number was {num}")


