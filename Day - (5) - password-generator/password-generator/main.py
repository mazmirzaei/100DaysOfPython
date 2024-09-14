#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#random letter generator
def pass_generator():
    
    ran_letter = []
    for num in range(0,nr_letters):
        ran_letter.append(random.choice(letters) ) 

    ran_symbols = []
    for num in range(0,nr_symbols):
        ran_symbols.append(random.choice(symbols) ) 

    ran_numbers = []
    for num in range(0,nr_numbers):
        ran_numbers.append(random.choice(numbers) ) 

    ran_pass=[]
    ran_pass = ran_letter + ran_symbols + ran_numbers
    random.shuffle(ran_pass)
    
    password = ''
    for item in ran_pass:
        password +=item
    return password
print(pass_generator())