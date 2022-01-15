from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        choice = random.randint(1, 6)
        if choice == 1:
            new_car = Turtle("square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            new_car.speed("fast")
            self.car_list.append(new_car)

    def move_car(self):
        # we're moving every car appended in list with constant speed
        for car in self.car_list:
            car.forward(self.speed)

    def increment(self):
        # increase the speed every time it reaches nest level
        self.speed += MOVE_INCREMENT
        for car in self.car_list:
            car.forward(self.speed)



