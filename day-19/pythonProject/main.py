import random
from turtle import Turtle, Screen

# Create the turtle and screen
screen = Screen()
screen.setup(width=500, height=400)  # Adjust the size if necessary
user_bet = screen.textinput(title="Make your bet", prompt="Please insert your bet")

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
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")

# Exit on click
screen.exitonclick()  # Click to exit