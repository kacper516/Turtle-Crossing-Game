import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    player.finish()

    car_manager.create_car()
    car_manager.move_car()

    # detect with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20: # because car is 20px width
            game_is_on = False
            scoreboard.game_over()

    if player.finish():
        player.reset_turtle()
        scoreboard.refresh_score()
        car_manager.speed_up()


screen.exitonclick()