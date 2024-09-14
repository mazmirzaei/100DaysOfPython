import User
from flask import Flask
app = Flask(__name__)


# set FLASK_APP=hello.py
# flask run
# '/' mean home page
@app.route('/')
def hello_world():
    return 'Hello, World'


# makes the word bold
def make_bold(function):
    def wrapper_func():
        word = function()
        return f'<b>{word}<b>'
    return wrapper_func

# make the word italic
def make_emphasis(function):
    def wrapper_func():
        word = function()
        return f'<em>{word}<em>'
    return wrapper_func

# make the word underline
def make_underLine(function):
    def wrapper_func():
        word = function()
        return f'<u>{word}<u>'
    return wrapper_func


@app.route('/bye')
@make_bold
@make_emphasis
@make_underLine
def say_bye():
    return "bye!"

#<variable> is a take in value
# http://127.0.0.1:5000/username/Maz/20
@app.route('/username/<name>/<int:number>')
def greeting(name, number):
    return f"Hello {name} !, you are {number} years old!"


@app.route('/kitty')
def gif_pics():
    return '<h1> Hello Kitty</h1>' \
           '<p>This is a gif</p>' \
           '<img src="https://giphy.com/gifs/cat-smoke-smoking-3o6Zt481isNVuQI1l6" width=200>'






# it mean run from current file 
if __name__ == "__main__":
    # same as flask run in terminal
    # Run the app in debug mode to auto_reload
    app.run(debug=True)
    