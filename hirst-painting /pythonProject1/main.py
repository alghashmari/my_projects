import turtle
import random

# Create a list to store the RGB tuples
rgb_color_list = [
    (203, 172, 107), (218, 225, 232), (238, 245, 242), (153, 181, 196),
    (193, 161, 177), (152, 186, 174), (214, 204, 111), (208, 179, 196),
    (174, 189, 213), (161, 203, 216), (160, 214, 187), (114, 123, 186),
    (178, 161, 71), (213, 182, 180), (98, 98, 97), (41, 41, 41),
    (94, 92, 93), (201, 207, 43), (53, 51, 52), (130, 127, 128),
    (105, 105, 107), (66, 63, 64)
]

# Step 1: Set up the screen first to avoid canvas issues.
screen = turtle.Screen()
screen.colormode(255)  # Enable RGB colors

# Step 2: Set up the turtle after initializing the screen.
tim = turtle.Turtle()
tim.shape("turtle")
tim.penup()  # Pen up to avoid drawing lines
tim.speed("fastest")  # Speed up the turtle

# Set the starting position of the turtle
starting_x, starting_y = -250, -250
tim.goto(starting_x, starting_y)

# Function to draw a dot of size 20 with random color
def draw_dot():
    random_color = random.choice(rgb_color_list)
    tim.dot(20, random_color)

# Function to move turtle to the next row
def move_to_next_row(y_position):
    tim.penup()  # Ensure the pen is up
    tim.goto(starting_x, y_position)  # Move to the starting position of the next row

# Main function to draw the 10x10 dot grid
def draw_grid(rows, columns, dot_distance):
    y_position = starting_y
    for _ in range(rows):
        for _ in range(columns):
            draw_dot()  # Draw the dot
            tim.forward(dot_distance)  # Move forward by dot_distance
        # After completing a row, move to the next row
        y_position += dot_distance
        move_to_next_row(y_position)

# Call the function to draw the grid (10x10, with dots spaced 50 apart)
draw_grid(10, 10, 50)

# Step 3: Exit the program when you click on the screen
screen.exitonclick()