# import random
# # creating a list
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # computer random choosing
# computer_choice = random.randint(0,9)
#
# # user choice
# user_choice = int(input("choose a number between 0-10\n"))
# print(f"You chose: {user_choice}")
#
# if user_choice == computer_choice:
#     print("Congrats you won")
# else:
#     print("sorry try again")
#
#

# # creating a list
# operations = ["+", "-", "*","/"]
# # asking user picking operation
# choice_1 = input("pick one of following +, -, *, / \n")
#
# # user picking two number
# choice_2 = float(input("choose first number\n"))
# choice_3 = float(input("choose second number\n"))
#
# # Performing the operation
# if choice_1 == "+":
#     result = choice_2 + choice_3
# elif choice_1 == "-":
#     result = choice_2 - choice_3
# elif choice_1 == "*":
#     result = choice_2 * choice_3
# elif choice_1 == "/":
#     # Handle division by zero
#     if choice_3 != 0:
#         result = choice_2 / choice_3
#     else:
#         result = "Error! Division by zero is not allowed."
# else:
#     result = "Invalid operation!"
#
# # Print the result
# print(f"The result is: {result}")
#
# # creating a list.
conversion_type = ["C to F", "F to C", "C to K", "K to C"]
#
# # asking user for inputs
# temperature = float(input(" what is the temperature you would like to convert"))
# choose_type = int(input("choose the type to convert 0 - 3"))
# print(conversion_type[choose_type])
#
# # creating formulas
# result = 0
# if choose_type == 0:
#     result = (1.8 * temperature) + 32
#     print(result)
# elif choose_type == 1:
#     result = 0.5555 * ( temperature -32)
#     print(result)
# elif choose_type == 2:
#     result = temperature + 273.15
#     print(result)
# else:
#     result = temperature - 273.15
#
# # last input
# input(" would you like to perform another conversion\n")

while True:
    # Displaying the conversion options
    print("Choose a conversion type:")
    for i, conversion in enumerate(conversion_type, start=1):
        print(f"{i}. {conversion}")

    # Asking user to select a conversion type by number or name
    user_input = input("Enter the number or name of the conversion type: ").strip()

    # Determine the conversion type based on user input
    if user_input.isdigit():
        choice = int(user_input) - 1
        if 0 <= choice < len(conversion_type):
            conversion_selected = conversion_type[choice]
        else:
            print("Invalid selection.")
            continue
    elif user_input in conversion_type:
        conversion_selected = user_input
    else:
        print("Invalid selection.")
        continue

    # Asking for the temperature to convert
    temperature = float(input("Enter the temperature to convert: "))

    # Performing the conversion
    if conversion_selected == "C to F":
        result = (1.8 * temperature) + 32
    elif conversion_selected == "F to C":
        result = (temperature - 32) * 5 / 9
    elif conversion_selected == "C to K":
        result = temperature + 273.15
    elif conversion_selected == "K to C":
        result = temperature - 273.15

    # Display the result
    print(f"The result is: {result:.2f}")

    # Ask the user if they want to perform another conversion
    another_conversion = input("Would you like to perform another conversion? (yes/no): ").lower()
    if another_conversion != "yes":
        break



