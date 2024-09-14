programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function":
    "A piece of code that you can easily call over and over again.",
}
print(programming_dictionary)

#add a key: value to a dic
programming_dictionary['Error'] = ' error'
print(programming_dictionary)

#How to loop to a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Challenge 1 dictionary
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

#nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
#list nested dictionary
travel_log = {
    'Farnce': ['Paris', 'Lille', 'Dijan'],
    "Germany": ['Berlin', "hamburg"]
}

#dictionary nested dictionary

travel_log1 = {
    "Farnce": {
        'cities visdited': ['Paris', 'Lille', 'Dijan'],
        'total_visited': 3
    },
    "Germany": {
        'cities visited': ['Berlin', "hamburg"],
        'total_visited': 2
    },
}

# nested dictionery inside a list
list_dictionaries = [{
    "Farnce": {
        'cities visdited': ['Paris', 'Lille', 'Dijan'],
        'total_visited': 3
    },
    "Germany": {
        'cities visited': ['Berlin', "hamburg"],
        'total_visited': 2
    }
}, {
    'Farnce': ['Paris', 'Lille', 'Dijan'],
    "Germany": ['Berlin', "hamburg"]
}]


#nesting Challenege 2 : 
# write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.


travel_logs = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(countery_visited, number_visited,cities_visited):
    new_countery ={}
    new_countery['country'] = countery_visited
    new_countery['visits'] = number_visited
    new_countery['cities'] = cities_visited
    travel_logs.append(new_countery)




#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_logs)



