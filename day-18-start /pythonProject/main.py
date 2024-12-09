import turtle
import random

# Set up the turtle
tim = turtle.Turtle()
tim.shape("turtle")
tim.speed("fastest")  # Set the speed to the fastest

# Set color mode to 255 to allow RGB color setting
turtle.colormode(255)

# Create the screen object
screen = turtle.Screen()

# Function to generate random RGB color values
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Function to draw the spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):  # Calculate how many circles to draw
        tim.color(random_color())  # Set random color
        tim.circle(100)  # Draw a circle with radius 100
        tim.setheading(tim.heading() + size_of_gap)  # Tilt the heading by the gap

# Call the function to draw the spirograph
draw_spirograph(5)  # You can change the gap size (e.g., 5, 10, etc.)

# Keep the window open until clicked
screen.exitonclick()