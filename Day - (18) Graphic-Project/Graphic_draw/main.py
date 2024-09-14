import turtle
from turtle import Screen
import random


tim = turtle.Turtle()
tim.shape("turtle")
tim.color("Blue")

######################################### draw dashed line ##############################
for n in range(0,4):
    tim.forward(100)
    tim.left(90)

for n in range(20):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)

################################### Shape draw ###########################################


colors = ['blue', 'blue1', 'blue2', 'blue3', 'blue4', 'blue5']


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for side in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shapes(shape_side)



################################################## Draw random direction ##########################################


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


angles = [90, 180, 360]
tim.pensize(10)
tim.speed(50)

for n in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(angles))


############################## Make A Spirograph #######################
import turtle as t
from turtle import Screen
import random


tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

tim.speed('fastest')


def draw_spirograph(size_of_gap):
    for n in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()