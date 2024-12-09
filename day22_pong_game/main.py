from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Paddle controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # Collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    if (ball.distance(r_paddle) < 60 and ball.xcor() > 320) or (ball.distance(l_paddle) < 60 and ball.xcor() < -320):
        ball.bounce_x()

    # Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Winning condition
    if scoreboard.l_score == 5:
        scoreboard.goto(0, 0)
        scoreboard.write("Left Player Wins!", align="center", font=("Courier", 36, "bold"))
        game_is_on = False

    if scoreboard.r_score == 5:
        scoreboard.goto(0, 0)
        scoreboard.write("Right Player Wins!", align="center", font=("Courier", 36, "bold"))
        game_is_on = False

    screen.update()

screen.exitonclick()