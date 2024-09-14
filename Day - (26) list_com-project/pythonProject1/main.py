# list comprehensions
# new_list = [new_item for item in list]

numbers = [1, 1,2,3,5,8,13,21,34,55]
new_list=[]
for num in numbers:
    new_item = num + 1
    new_list.append(new_item)
print(new_list)

# using list com
new_list1 = [num + 1 for num in numbers]
print(new_list1)

name = 'angela'
name_list = [letter for letter in name]
print(name_list)

new_range = [num*2 for num in range(1,5)]
print(new_range)

# Condition list Comprehension
# new_list = [new_item for item in list if test]
names = ['Alex', 'Max', "Madonna", 'James', "Maziyar"]
short_names = [name for name in names if len(name) < 4]
print(short_names)

long_names = [name for name in names if len(name) > 4]
print(long_names)


# You are going to write a List Comprehension 
# to create a new list called squared_numbers.
# This new list should contain every number in the 
# list numbers but each number should be squared.
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# You are going to write a List Comprehension to create a new list called result. 
# This new list should only contain the even numbers from the list numbers.
result = [num for num in numbers if num%2 == 0]
print(result)

#  Take a look inside file1.txt and file2.txt. 
#  They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which 
# contains the numbers that are common in both files.

#  file one 
with open("file1.txt") as fileOne:
    nums = fileOne.readlines()
num_one = [ int(num.strip()) for num in nums] 
print(num_one)

# file two
with open('file2.txt') as fileTwo:
    nums = fileTwo.readlines()
num_two = [int(num.strip())for num in nums]
print(num_two)

#  using for loop
same_num = []
for num1 in num_one:
    if num1 in num_two:
        same_num.append(num1)
print(same_num)

# using list compression
same_num1 = [num for num in num_one if num in num_two]
print(same_num1)

############################### Dictionary Comprehension ###############################
# new_dict = {new_key : new_value for item in list}
# new_dict = {new_key : new_value for (key, value) in dict.items() if test}
import random

students_score = {students: random.randint(50,100) for students in names}
print(students_score)

passed_students = {students: score for (students, score) in students_score.items() if score >= 70}
print(passed_students)

######################################## Challenges ###################################################
# You are going to use Dictionary Comprehension 
# to create a dictionary called result that takes each
# word in the given sentence and calculates the number of letters in each word.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
dictionary_word = {word: len(word) for word in sentence.split(' ')}
print(dictionary_word)


######################################### Challenege 2 #################################################
# You are going to use Dictionary Comprehension to create a 
# dictionary called weather_f that takes each temperature 
# in degrees Celcius and converts it into degrees Farenheight.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# (temp_c * 9/5) + 32 = temp_f
weather_f = {day: (temp*9/5)+32 for day, temp in weather_c.items()}
print(weather_f)

