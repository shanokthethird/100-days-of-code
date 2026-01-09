from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280
CAR_IMAGE = 'street3.png'
TURTLE_IMG = 'TURTLE.gif'

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.addshape(TURTLE_IMG)
        self.shape(TURTLE_IMG)
        self.penup()
        self.speed('fastest')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_back(self):
        if self.ycor() > -20:
            self.goto(STARTING_POSITION)

    def listing(self, car_list):
        if len(car_list) > 0:
            self.carlist = car_list

    def up(self):
        if len(self.carlist) > 0:
            if self.carlist[0].xcor() < 0:
                self.forward(MOVE_DISTANCE)

    def down(self):
        self.back(MOVE_DISTANCE)

    def background_pic(self, param=CAR_IMAGE):
        self.screen.bgpic(param)
