fruits = ['apple', 'peach', 'pearl']

for item in fruits:
    print(item + ' pie')
    print(fruits)
print(fruits)

############################################################################Challenge 1 in for loop
# write a program that calculates the average student height from a List of heights.

#get the list from the user and covert it to int data type

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum  = 0
for student in student_heights:
    sum += student
    avg = (sum/len(student_heights))
print(avg)

# or 
avg = round(sum(student_heights)/len(student_heights),2)
print(avg)

############################################################################
#Challeneg 2 :
#Write a program that calculates the highest score from a List of scores.
student_scores = input("Enter a list of student scores :  ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
max = 0
for n in range(0, len(student_scores)-1):
    if student_scores[n] >= student_scores[n+1]:
        max = student_scores[n]
    else:
        max = student_scores[n+1]
print(max)
#___________________________________________________________
#another version: 
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)
    
print(f"The highest score in the class is: {highest_score}")

############################################################################
#range 
#sum of number from 0 to 100
total = 0
for n in range(0,101):
    total +=n
print(total)
###########################################################################
#range Challeneg : 
# write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100.
sum_number=0
for n in range(0, 101, 2):
    sum_number += n
print(sum_number)

###########################################################################
#FizzBuzz Challenege : 
#write a program that automatically prints the solution to the FizzBuzz game.
#Your program should print each number from 1 to 100 in turn.

#When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#`When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
#  `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
for num in range(1,101): 
    if  num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Buzz')
    elif num % 5 == 0:
        print('Fizz')
    else:
        print(num)
