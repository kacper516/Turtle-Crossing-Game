from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """This function will create new_car"""
        if_create = random.randint(1, 6)  # to make less cars so player can win
        if if_create == 3:  # random value i choose 3
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))  # to set random color
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(305, random.randint(-250, 250))  # x is hardcoded to 305 to leave the screen
            self.all_cars.append(new_car)

    def move_car(self):
        """This function will move te x cor of cars"""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        """When player reach the finish, cars start to go a little bit faster"""
        self.car_speed += MOVE_INCREMENT
