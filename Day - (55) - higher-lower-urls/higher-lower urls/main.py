import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return "<h1> Guess a number between 0 and 9 </h1>" \
           "<img src='https://media0.giphy.com/media/l5Iz5PiVpa89lqOBil/200w.webp?cid=ecf05e47kfm9f948kaqqmooynz5qwvx0dkutwbqn6n01n6gu&rid=200w.webp'> "

# generates random number
random_number = random.randint(0,10)

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    
    else:
        return"<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"



if __name__  == '__main__':
    app.run(debug=True)
