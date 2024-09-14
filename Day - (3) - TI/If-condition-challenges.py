#Condition
#Challege 1 :
#Write a program to check if your number is odd or even

user_input = int(input("Please enter a number to check if the number is odd or even : "))
def odd_even(user_input):
    if user_input % 2 == 0 :
        return f"The number {user_input} is even."
    else:
        return f"The number {user_input} is odd. "

print(odd_even(user_input))

#################################################################################################
#Challenege 2 : 
#wirte a program that body mass

user_weight = int(input("Please enter your weight in  kg ex. 150 : "))
user_height = float(input("Please enter your height in this form ex. 1.75 for 175cm : "))
def bmi(user_weight , user_height):
    bmi = round(user_weight/(user_height**2),2)
    if bmi < 18.5:
        return f"You are unederweight and your bmi is {bmi}"
    elif bmi == 18.5 and bmi < 25:
        return f"You are normal and your bmi is {bmi}"
    elif bmi > 25 and bmi < 30:
        return f"You are overwhight and your bmi is {bmi}"
    elif bmi > 30 and bmi < 35:
        return f"You are obese and your bmi is {bmi}" 
    else:
        return f"You are clinicly obese and your bmi is {bmi}"

print(bmi(user_weight , user_height))

#################################################################################################
#Challenege 3: 
#Write a program if a year is a leap or not

year = int(input("Enter a year to see if is a leap year or not : "))
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"The year {year} is  a leap year, it has 366 days"
            else:
                return f"The year {year} is not a leap year, it has 365 days"
        else:
            return f"The year {year} is  a leap year, it has 366 days"
    else:
        return f"The year {year} is not a leap year, it has 365 days"

print(leap_year(year))


#################################################################################################
#Challenege 4: 
#Order Pizza 

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

########################################################
#Challenge 5 
# write a program that tests the compatibility between two people. We're going to use the super scientific method recommended by BuzzFeed.
print("Welcome to the Love caculator")
user1=input("What is your name? : ").lower()
user2=input("What is your partner name ? : ").lower()
true = "true"
love = "love"
u1=0 
u2=0 
t1=0 
t2 = 0
l1=0 
l2=0 
r1=0 
r2 = 0

for char in true:
    u1 = user1.count(char)
    t1 += u1
    u2 = user2.count(char)
    t2 += u2
t_true = t1 + t2

for char in love:
    r1 = user1.count(char)
    l1 += r1
    r2 = user2.count(char)
    l2 += r2
l_love = l1 + l2

score =int(str(t_true) + str(l_love))
#print(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >=40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

####################################################################################################################################################
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = ''
combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


#######################################################################