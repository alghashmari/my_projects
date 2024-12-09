import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Keybindings
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Car management
    car_manager.create_car()
    car_manager.move_cars()

    # Collision detection
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Level progression
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()