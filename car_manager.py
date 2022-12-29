from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = 360

CARS = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLORS[random.randint(0,5)])
        self.shape("square")
        self.shapesize(1,2)
        global position
        position = random.randint(-260, 260)
        self.goto(340, position)

    def spam_car(self):
        self.new_car = CarManager()
        CARS.append(self.new_car)

    def move_car(self):
        global position
        new_x = STARTING_POSITION - 10
        self.goto(new_x, position)