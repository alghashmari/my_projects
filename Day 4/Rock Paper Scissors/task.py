import random
from tempfile import tempdir

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#1 create a list
list1= [rock, paper, scissors]
# user to be a number
user_choice = int(input("pick a number 0,1 or 2"))
print(list1[user_choice])

# computer choice.
# computer_choice = random.randint(0,2)
# print(computer_choice)
# print(list1[computer_choice])
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")

