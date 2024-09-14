# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# The parameter is the name of the data that's being passed in,
# The argument is the actual value of the data. Now,

def greet_with_name(parameter):
    print(f"Hello {parameter}")

greet_with_name('argument')


#function with more than one input
def greet_with(name,location):
    print(f'My name is {name} and my locarion is {location}')

greet_with('Maz',"La jolla")


#call function with keyword argumnets
greet_with(name='Maz', location='La jolla')

import math
#function Challenege 1 : 
def can_calc(w, h):
    area = w * h
    covearge = 5
    num_cans = area / covearge
    return math.ceil(num_cans)
    
print(can_calc(7, 13))

#Prime number checkr function
num = int(input("Enter a number to check if is it prime : "))
def prime_checker(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")
            
        # if input number is less than
        # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")

prime_checker(num)