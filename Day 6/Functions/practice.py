# import random
# from audioop import reverse
#
# from itertools import count
# from operator import countOf
# from stringprep import in_table_c9

#
#
#
# # Welcome message
# print("welcome to our little game!")
# # creating computer number
# computer_random = random.randint(1,100)
# # user number choosing
# user_number = int(input("choose a number between 1-100?\n"))
# # #if elif and else
# while user_number != computer_random:
#     if user_number < computer_random:
#         print("your guess is lower than computer")
#     elif user_number> computer_random:
#         print("your guss is higher than computer")
#         # Ask for another guess inside the loop
#     user_number = int(input("Try again! Choose a number between 1 and 100:\n"))
# # Congratulatory message when guessed correctly
# # print("Hooray! You guessed right!")

# # welcoming message
# print("welcome to our little game")
# #user questions
# paragraph = input("insert your paragraph of text\n")
# words = paragraph.split()
# word_count = len(words)
# print(word_count)

# # use choosing number
# user = int(input("guess a number between 1-100?\n"))
#
# # computer gussing
# c_g = random.randint (1,10)
# attempts = 1
# # using if elif and else
# while user != c_g:
#
#     if user < c_g:
#      print("your guess is lower")
#     elif user> c_g:
#         print("your guess is higher")
#     attempts += 1
#     user = int(input("try again! guess a number between 1-100?\n"))
# print("Hooray! You guessed right!")
#
# print(f"your total attempts is {attempts}")
#
# ask use how many numbers
# times_chosen = int(input("how many number you want to enter?\n"))
#
# #
# i = 10
# while i >=1:
#     print(i)
#     i-=1

# i = 2
# while i % 2 ==0 :
#     print(i)
#     i+=2

# i = 2
# print("below are all the even numbers 1-10")
# while i<= 10:
#     print(i)
#     i+=2
# print("below are all the odd number 1-10")
# i = 1
# while i <= 10:
#     print(i)
#     i+=2
# i = 10
# sum_t=[]
# while i <=10:
#
#     i=i+i
#     sum_t.append(i)
# print(sum_t)

# i = 1
# while i <= 10:
#     if i%2==0:
#         print(i)
#     i += 1
# number = int(input("pick a number"))
# while number >1:
#     print(number)
#     number = number/2
#
# answer = input("Choose a word: ")
#
# while answer != "exit":
#     print(answer)
#     answer = input("Choose a word: ")
#
#
# secret =random.randint(1,10)
# # print(secret)
# answer =int(input("prick a number between 1-10"))
# while secret != answer:
#     answer = int(input("wrong guess again"))
#     print(secret)
#     print("you won!")
# number = int(input("pick a number "))
# while number >= 1:
#     print(number)
#     number-=1
# number = 0
# while number <= 100:
#     print(number)
#     number +=2
# i = 10
# while i>=1:
#     print(i)
#     i-=1
# number = int(input("pick a number"))
# while number >= 1:
#     print(number)
#     number -= 1
# number = input(input("enter a number"))
# while number >= 1:
#     print(number)
# print("wrong entry pick again")
# number = int(input("pick a number"))
# i= 1
# while i <= number:
#     print(number + i)
#     i+=1
# total_count = []
# user_pick = int(input("pick a number"))
# while user_pick != 0:
#     user_pick = int(input("pick a number"))
#     total_count.append(user_pick)
# print(len(total_count))
# secret = "python123"
# password = input("enter a password")
# while password != secret:
#     password= input("wrong! enter a password")
# print("congrats you did it!")

# guess = int(input("pick a number"))
# total = []
# while guess > 0:
#     total.append(guess)
#     guess = int(input("pick a number"))
# print(sum(total))
# i = 1
# while i <=10:
#     print(i*i)
#     i+=1

# i = 1
# while i <=10:
#     print(3*i)
#     i+=1

# i = 1
# while i <= 10:
#     print(i)
#     i+=1
# number = int(input("pick a number\n"))
# attempts =0
# while number >=0:
#     number = int(input("pick a number\n"))
#     attempts +=1
# print("sorry! you ended the  loop")
# print(f"your total attempts is {attempts}")

user_number = int(input("pick a number > 2\n"))
sum_even = []
i = 1
while user_number >= 2:
    if user_number % 2 == 0:
        sum_even.append(user_number)
        user_number = int(input("pick a number > 2\n"))
print(sum(sum_even))
