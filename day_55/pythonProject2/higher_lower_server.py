from flask import Flask
from random import randint

app = Flask(__name__)

random = randint(0,9)

def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'

    return wrapper


def make_italic(function):
    def wrapper():
        return '<em>' + function() + '</em>'

    return wrapper


def make_underline(function):
    def wrapper():
        return '<u>' + function() + '</u>'

    return wrapper


def make_H1(function):
    def wrapper():
        return '<h1>' + function() + '</h1>'

    return wrapper


def make_H2(function):
    def wrapper():
        return '<h2>' + function() + '</h2>'

    return wrapper


def make_central(function):
    def wrapper():
        return '<center>' + function() + '<center>'

    return wrapper



@app.route('/')
@make_H1
@make_central
@make_underline
def initial_page():
    return ('Guess a number between 0 and 9'
            '<p> </p>'
            '<img src="https://media2.giphy.com/media/v1'
            '.Y2lkPTc5MGI3NjExdjRhamJ2Mm04anN5Nm10aGlqdHpldTR2NzQ2ZXM3bTIza2NiZnVvZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY'
            '3Q9Zw/YnBntKOgnUSBkV7bQH/giphy.gif">')

@app.route('/<int:number>')
# @make_H1
# @make_bold
# @make_underline
def page_1(number):
    if number > random:
        return ('<h1><center><b>Too high</h1></center></b>'
                '<p> </p>'
            '<center><img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExanFhbXEzOXJmbGZjOWh3bTF3aWZ5eGF3aGRlaWM2MjkzMXIyc2tweCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SyemapFxj7TiM/giphy.gif"></center>')
    elif number < random:
        return ('<h1><center><b>Too low</h1></center></b>'
                '<p> </p>'
            '<center><img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGt1bWgydGxxdWZnMTVmaWpmY3M5bmsyN3o3bXc1MmNjeGF2NjMyMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif"></center>')
    else:
        return ('<h1><center><b>You found me, bastard</h1></center></b>'
                '<p> </p>'
                '<center><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWhrYmd5ajcxMjBsNzU3b20xMG82dTByb3UxZ29yeDA2Y292eTR3NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMR5B0fQJe5S5nW/giphy.gif"></center>')

if __name__ == "__main__":
    app.run(debug=True)
