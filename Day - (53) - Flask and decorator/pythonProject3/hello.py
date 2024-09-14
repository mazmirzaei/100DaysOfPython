from flask import Flask
app = Flask(__name__)


# set FLASK_APP=hello.py
# flask run
# '/' mean home page
@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route("/bye")
def say_bye():
    return "bye"


# it mean run from current file 
if __name__ == "__main__":
    # same as flask run in terminal
    app.run()
    