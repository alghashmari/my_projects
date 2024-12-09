# range function with for loop
# for number in range (1,10):
#     print(number)
# total = 0
# for number in range(1,101):
#
#     total += number
# print(total)
# for in 1 -100
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10]
for number in range(1, 101):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")

    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")

    else:
        print(number)
#
# # Create a loop with For and Range to go from 1 to 100.
# for number in range(1, 101):
#     # First check if the number is divisible by both 3 and 5.
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#
#     # Then check if the number is only divisible by 3
#     elif number % 3 == 0:
#         print("Fizz")
#
#     # Finally check if the number is only divisible by 5
#     elif number % 5 == 0:
#         print("Buzz")
#
#     If it's not divisible by either of those numbers, just print the number
#     else:
#         print(number)



