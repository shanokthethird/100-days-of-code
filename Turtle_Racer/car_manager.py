from random import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

IMAGES = ['car1.gif', 'car2.gif', 'car3.gif']

positions = []
for x in range(-260, 260, 20):
    positions.append(x)


class CarManager:
    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10

    def create_car(self):
        car = Turtle('square')
        car_img = choice(IMAGES)
        car.screen.addshape(car_img)
        car.shape(car_img)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        # car.color(choice(COLORS))
        car.penup()
        car.goto(300, choice(positions))
        self.cars.append(car)

    def cars_forward(self, position):
        for vehicles in self.cars:
            vehicles.forward(self.STARTING_MOVE_DISTANCE)
            if vehicles.xcor() <= -300:
                vehicles.hideturtle()
                self.cars.remove(vehicles)
        if position >= 280:
            self.STARTING_MOVE_DISTANCE += self.MOVE_INCREMENT
