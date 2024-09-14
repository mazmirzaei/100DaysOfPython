#Data Types, 
###############################################################################################
#String
print("Hello"[0])
#or
string = 'Hello'
print(string[0])
print('123'+'456')

#Integer, numbers without decimals
#python ignores the underline character
print(123_456_789+236_464_66)

#float
3.12

#boolean
# True, False

num_char = len(input("What is your name ? "))
print(type(num_char))

###############################################################################################
#convert datatypes : 

#int to str
a = 123
a_str = str(a)
print(type(a_str))

#int to float
b = 123
b_float = float(b)
print(b_float)

#str to int
c = '654'
c_int = int(c)
print(c)

###############################################################################################
#Challenge1 : 
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8


def two_digit(number):
    str_input = str(number)
    num1 = int(str_input[0])
    num2 = int(str_input[1])
    result = num1 + num2
    return result
    
print(two_digit(35))

###############################################################################################
#operation PEMDAS (), **, * / , + - 
# // divison the output is int
# / the output is float

###############################################################################################
#Challenge2:
#BMI Calculator 
#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#BMI = weight/height**2

weight = float(input('Plases enter your weight in KG : '))
height = float(input('Please enter you height in m : '))
#round to two digit decimal
BMI = round(weight/(height**2),2)
print(f"your BMI with weight :  {weight} and height :  {height} is  : {BMI}")


###############################################################################################
#Challange3: 
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
def until_90(age):
    ninty = 90
    remaning = 0 
    remaning = ninty - age
    months = remaning * 12
    weeks = months * 4 
    days = weeks * 7

    print(f"Your age is {age} and you have {months} months {weeks} weeks and, {days} days until you are 90")

###############################################################################################

