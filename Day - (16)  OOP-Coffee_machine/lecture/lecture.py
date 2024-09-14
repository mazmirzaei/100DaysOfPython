from turtle import Turtle, Screen
# the turtle
timmy = Turtle()
# shape of the timmy
timmy.shape('turtle')
timmy.color("coral")
# moving method
timmy.forward(100)

# The Screen
my_screen = Screen()
# height of the canvas for my_screen variable
print(my_screen.canvheight)
my_screen.exitonclick()

#############################################################################################################################
#
# table
from prettytable import PrettyTable
table = PrettyTable()
pokemon_name = ['Picachu', 'Squirtele', 'Charmander']
pokemon_type = ['Electric', 'Water', 'Fire']
table.add_column('PokeMon names', pokemon_name)
table.add_column('Type', pokemon_type)
# left hand align
table.align = 'l'
print(table)





