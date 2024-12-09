# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("welcome to the rollercoster!")
# else:
#     print("please come next year!")
#
# # greater or equal
# # == equal to
# # != not equal to

number = int(input("Choose a number\n"))
if number % 2 == 0:
    print("This is an even number\n")
else:
    print("This is an odd number\n")

again = input("Would you like to repeat the process? Y/N\n").lower()
if again != "y":
    print("Thanks for trying\n")
