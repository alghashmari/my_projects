# phase 1
from logging import fatal
from socket import fromfd



from art import logo



def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
# phase 2
ops = {"+":add,"-":sub, "*":mul, "/":div}

def calculator():
    # Program asks the user to type the first number.
    n1 = float(input("Type your first number: "))
    should_continue = True

    while should_continue:
        # Program asks the user to type a mathematical operator
        choose = input(f"Choose your math operator {list(ops.keys())}: ")
        # Program asks the user to type the second number.
        n2 = float(input("Type your second number: "))
        # Program works out the result based on the chosen mathematical operator.
        result = ops[choose](n1, n2)
        print(f"Result: {result}")

        # Program asks if the user wants to continue working with the previous result.
        repeat = input("Would you like to continue working with the previous result (y/n)? ").lower()
        if repeat == "y":
            n1 = result
        else:
            # If no, the program restarts by asking for the first number again.
            should_continue = input("Do you want to start a new calculation (y/n)? ").lower() == "y"
            if should_continue:
                calculator()  # Restart the calculator

# Run the calculator
calculator()