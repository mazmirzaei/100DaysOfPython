import random 
import my_module

print(my_module.pi)

random_int = random.randint(1,10)
print(random_int)

#######random float
#######Creates random number beteen 0.0000 - 0.99999
float_random = random.random() 
print(float_random)

#######Creates random number between 0.0000 - 4.9999
f_rand = random.random()
print(f_rand * 5)

####Chalenege 1
# write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
print('Lets Play! ')
answer = 'yes'
while answer == 'yes':
    h_t = random.randint(0,1)
    if h_t == 0:
        print('Head')
    else:
        print('Tail')
    answer = input('Do you want to again ? ')
else:
    answer = 'no'
    
#######################################################################
############################  List  ###################################
#######################################################################
#https://docs.python.org/3/tutorial/datastructures.html

stats_of_America = ['Ca','Ar','Nv','Az']
print([0])
print([1])
print([2])
# #change items in the list
stats_of_America[0] = "CA"
stats_of_America[1] = "AR"
stats_of_America[2] = "NV"

# #add item to the end of the list 

stats_of_America.append('NY')
stats_of_America.append('WA')

#Challenege 1 list
#write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
names_string =input('enter names with a comma : ')
names = names_string.split(',')
ran = random.randint(0, len(names)-1)
print(f"The Person pay the bills is : {names[ran]}")

##########################################################################
#Chalenege 2
#write a program which will mark a spot with an X in the map below
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
p1 = int(position[0])
p2 = int(position[1])
map[p1-1][p2-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")


###########################################################################

