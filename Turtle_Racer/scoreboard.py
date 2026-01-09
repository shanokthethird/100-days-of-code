from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT2 = ("Courier", 40, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.color('black')
        self.goto(x=-20, y=265)
        self.update()

    def update(self, score=0):
        self.clear()
        self.write(f'Level {score + 1}', False, 'center', FONT)

    def game_over(self):
        jim = Turtle()
        jim.penup()
        jim.hideturtle()
        jim.goto(0, 20)
        jim.write("""GAME OVER""", False, 'center', FONT2)
