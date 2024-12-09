import random  # Import the random module for generating random numbers
from turtle import Turtle  # Import the Turtle class from the turtle module

class Food(Turtle):
    # Class to represent the food for the snake game, inheriting from Turtle
    def __init__(self):
        super().__init__()  # Initialize the parent class (Turtle)
        self.shape("circle")  # Set the shape of the food to a circle
        self.penup()  # Disable drawing when the food moves
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the food smaller (half the size of a default turtle)
        self.color("blue")  # Set the color of the food to blue
        self.speed("fastest")  # Set the food's speed to the fastest for instant updates
        self.refresh()  # Place the food at a random position on the screen

    def refresh(self):
        # Move the food to a new random position on the screen
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate within the screen bounds
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate within the screen bounds
        self.goto(random_x, random_y)  # Move the food to the generated random position