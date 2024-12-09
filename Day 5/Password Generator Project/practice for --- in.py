import random

# creating lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#  asking user for inputs
# letter_n = int(input("How many letters would you like in your username?\n"))
# number_n = int(input("How many numbers would you like in your username?\n"))
# symbols_n = int(input("How many symbols would you like in your username??\n"))
#
# # easy solution
# # For in and random
# user_name=""
# for user in range(0,letter_n):
#     user_name += random.choice(letters)
# for user in range(0,number_n):
#     user_name += random.choice(numbers)
# for user in range(0,symbols_n):
#     user_name += random.choice(symbols)
#     # print(user_name)
#
# # Convert the string to a list to shuffle
# user_name_list = list(user_name)
#
# # Shuffle the list
# random.shuffle(user_name_list)
#
# # Convert the list back to a string
# final_username = ''.join(user_name_list)
#
# # Print the final shuffled username
# print("Your generated username is:", final_username)


 # asking user for inputs
letter_n = int(input("How many letters would you like in the local part of your email (before the @ sign)\n"))
number_n = int(input("How many numbers would you like in the local part?\n"))
symbols_n = int(input("How many symbols would you like in the local part?\n"))

email_id = ""
# starting with for in and random
for email in range(0,letter_n):
    email_id += random.choice(letters)
    # print(email_id)
for email in range(0,number_n):
    email_id += random.choice(numbers)
    # print(email_id)
for email in range(0,symbols_n):
    email_id += random.choice(symbols)
    # Convert the string to a list to shuffle
    email_id_list = list(email_id)
    # Shuffle the list
    random.shuffle(email_id_list)

    # Convert the list back to a string
    final_email_id = ''.join(email_id_list)

    print(final_email_id)


