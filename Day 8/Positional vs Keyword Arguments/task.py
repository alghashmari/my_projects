# Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
#
# def greet_with_name (name, location):
#     print(f"hello{name}")
#     print(f"how is the weather in{location}")
# #
# # greet_with_name(" abdullah", " Jeddah")
#
# greet_with_name(location= " jeddah", name=" Abdullah")
from itertools import count


#
# # greet_with_name("Abdullah", "Jeddah")
#
# greet_with_name(location= "jeddah", name = "Abdullah")


# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
#
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
#
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
#
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
#
#
# calculate_love_score("Abdullah Alghashmari", "Sarah Alharthi")
# calculate_love_score(name1="abdullah", name2="sarah")

# def friend(name1, name2):
#     combined_names = (name1 + name2).lower()
#     f = combined_names.count("f")
#     r = combined_names.count("r")
#     i = combined_names.count("i")
#     e = combined_names.count("e")
#     n = combined_names.count("n")
#     d = combined_names.count("d")
#
#     count = f + r + i + e + n + d  # Calculate total count of the letters in 'FRIEND'
#     print(count)  # Print the score
#
#
# # Example usage
# name1 = input("Type your name: ")
# name2 = input("Type your mate's name: ")
# friend(name1, name2)


def counting(number1,number2):
    count = number1 + number2

counting(5,5)
print(count)
