MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Global variable for total money (profit)
total_money = 0
password = "1234"

# Check if enough resources are available for the drink
def has_sufficient_resources(drink_ingredients):
    """Returns True if resources are sufficient, False otherwise."""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# Deduct ingredients from resources after the drink is made
def make_drink(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# Process the coins and calculate the total inserted amount
def process_payment():
    """Prompt the user to insert coins and return the total value."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies

# Check if the transaction is successful and return change if needed
def validate_transaction(money_received, drink_cost):
    """Check if the payment is sufficient. If successful, return True, otherwise False."""
    if money_received < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is your change: ${change}")
        global total_money
        total_money += drink_cost
        return True

# Print a report of the current resources and total money
def print_report():
    """Display the machine's current resources and earnings."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_money}")

# Main loop to handle user interaction
def coffee_machine():
    """Main function to run the coffee machine."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            break
        elif choice == "report":
            report_password = input("Enter the password to access the report: ")
            if report_password == password:
                print_report()
            else:
                print("Access denied.")
        elif choice in MENU:
            drink = MENU[choice]
            if has_sufficient_resources(drink["ingredients"]):
                payment = process_payment()
                if validate_transaction(payment, drink["cost"]):
                    make_drink(choice, drink["ingredients"])
        else:
            print("Invalid choice, please try again.")

# Start the coffee machine
coffee_machine()