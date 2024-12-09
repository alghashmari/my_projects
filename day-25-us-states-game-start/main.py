import turtle

import pandas

ALIGN = "center"
FONT = ("Arial", 16, "normal")

# Set up the screen and map image
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read CSV file and initialize data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# Main game loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (Type 'Exit' to quit)"
    )

    if not answer_state:
        break

    # Normalize input for comparison
    answer_state = answer_state.title()

    # Exit and save missing states
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    # Handle duplicate guesses
    if answer_state in guessed_states:
        feedback_turtle = turtle.Turtle()
        feedback_turtle.hideturtle()
        feedback_turtle.penup()
        feedback_turtle.goto(0, -200)
        feedback_turtle.clear()
        feedback_turtle.write("You already guessed that state!", align=ALIGN, font=FONT)
        continue

    # Handle incorrect guesses
    if answer_state not in all_states:
        feedback_turtle = turtle.Turtle()
        feedback_turtle.hideturtle()
        feedback_turtle.penup()
        feedback_turtle.goto(0, -200)
        feedback_turtle.clear()
        feedback_turtle.write("State not found. Try again!", align=ALIGN, font=FONT)
        continue

    # Correct guess: Display on map
    guessed_states.append(answer_state)
    state_data = data[data.state == answer_state]
    x, y = state_data.x.item(), state_data.y.item()

    state_turtle = turtle.Turtle()
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(x, y)
    state_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))

# End game message
feedback_turtle.clear()
feedback_turtle.goto(0, -200)
feedback_turtle.write(f"Game Over! You guessed {len(guessed_states)}/50 states.", align=ALIGN, font=FONT)

screen.exitonclick()