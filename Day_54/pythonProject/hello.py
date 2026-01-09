from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper_func():
        return '<b>' + func() + '</b>'

    return wrapper_func


def make_italic(func):
    def wrapper_func():
        return '<em>' + func() + '</em>'

    return wrapper_func


def make_underline(func):
    def wrapper_func():
        return '<u>' + func() + '</u>'

    return wrapper_func


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def bye():
    return 'Bye'


if __name__ == "__main__":
    app.run(debug=True)
