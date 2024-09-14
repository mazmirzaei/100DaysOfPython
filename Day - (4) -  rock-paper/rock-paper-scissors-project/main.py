rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Lets Play rock, paper, scissors, ")
game = 5
n = 0
while n < game:
    user_pick = input("rock, paper, scissors ? : ").lower()
    com_rand = random.randint(0,2)
    if com_rand == 0:
        com_pick = 'rock'
    elif com_rand == 1:
        com_pick = 'paper'
    elif com_rand == 2:
        com_pick = 'scissors'

    if user_pick == 'rock' and com_pick == 'rock':
        print(rock)
        print(rock)
        print('Toss up')
    elif user_pick == 'rock' and com_pick == 'paper':
        print(rock)
        print(paper)
        print('You lost')
    elif user_pick == 'rock' and com_pick == 'scissors':
        print(rock)
        print(scissors)
        print('You won')
    elif user_pick == 'paper' and com_pick == 'rock':
        print(paper)
        print(rock)
        print('You Won')
    elif user_pick == 'paper' and com_pick == 'paper':
        print(paper)
        print(paper)
        print('Toss up')   
    elif user_pick == 'paper' and com_pick == 'scissors':
        print(paper)
        print(scissors)
        print('You Lost') 
    elif user_pick == 'scissors' and com_pick == 'scissors':
        print(scissors)
        print(scissors)
        print('Toss up') 
    elif user_pick == 'scissors' and com_pick == 'paper':
        print(scissors)
        print(paper)
        print('You won') 
    elif user_pick == 'scissors' and com_pick == 'rock':
        print(scissors)
        print(rock)
        print('You Lost') 
    n +=1
    print("Thank you")
  
        
