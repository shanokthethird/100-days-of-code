import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FONT = ("Courier", 20, "normal")

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
game_is_on = True
level = 0
player = Player()
player.background_pic()
key = 1
car = CarManager()
module = 3
screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down,'Down')
while game_is_on:
  if level>0:
    module = 2
  if level>5:
    module = 1
  if key%module == 0:
    car.create_car()
  car.cars_forward(player.ycor())
  for cars in car.cars:
    xcorlo = int(cars.xcor())-20
    xcorhi = int(cars.xcor())+20
    ycorlo = int(cars.ycor())-15
    ycorhi = int(cars.ycor())+15
      #print(int(player.ycor()) in range(ycorlo,ycorhi))
    if int(player.xcor()) in range(xcorlo,xcorhi):
      if int(player.ycor()) in range(ycorlo,ycorhi):
        score.game_over()
        game_is_on = False
  if level == 0:
    player.listing(car.cars)
  key+=1
  if player.ycor() >= 280:
    player.go_back()
    level+=1
    score.update(level)
    key = 0
  time.sleep(0.1)
  #if len(car.cars)>0:
  #  if car.cars[0].xcor() <= 0:
  screen.update()
screen.exitonclick()