import random
from turtle import Turtle, Screen

# Create the turtle and screen
screen = Screen()
screen.setup(width=500, height=400)  # Adjust the size if necessary
user_bet = screen.textinput(title="Make your bet", prompt="Please insert your bet")

# Ensure user input is clean and lowercase for comparison
user_bet = user_bet.lower().strip()

colors = ["hot pink", "pale violet red", "sienna", "blue violet", "lawn green", "dodger blue"]
y_position = [-50, -10, 30, 70, 110, 150]

all_turtles = []
# Create turtles and set their color/position
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False

# Start the race if user placed a bet
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Move each turtle a random amount
        movement = random.randint(0, 10)
        turtle.forward(movement)

        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor().lower()  # Convert winning color to lowercase for comparison

            # Create a turtle to display the result
            result_turtle = Turtle()
            result_turtle.hideturtle()  # Hide the turtle shape
            result_turtle.penup()  # Lift pen to avoid drawing

            if winning_color == user_bet:
                result_turtle.goto(0, 0)
                result_turtle.write(f"You have won! The {winning_color} turtle is the winner!", align="center",
                                    font=("Arial", 16, "normal"))
            else:
                result_turtle.goto(0, 0)
                result_turtle.write(f"You lost! The {winning_color} turtle is the winner!", align="center",
                                    font=("Arial", 16, "normal"))

# Exit on click
screen.exitonclick()  # Click to exit