print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

########
answer = 'yes'
while answer =='yes':
    user1 = input("left or right ? : ").lower()
    if user1 =='right' or user1 == '':
        print('Fall into a hole, Game Over')
        answer = input('Do you want to play again? yes or no : ')

    elif user1 == 'left':
        user2 = input('Swim or wait? : ').lower()
        if user2 == 'swim' or user2 =="":
            print('Attacked by trout, Game Over')
            answer = input('Do you want to play again? yes or no : ')
        elif user2 == 'wait':
            user3 = input('Which door? (red, blue, yellow, green): ').lower()
            if user3 == 'red':
                print('Burned by fire, Game Over')
                answer = input('Do you want to play again? yes or no : ')
            elif user3 =='blue':
                print('Eaten by beats, Game Over')
                answer = input('Do you want to play again? yes or no : ')
            elif user3 == 'yellow':
                print('You Win!')
            else:
                print('Game over')
                answer = input('Do you want to play again? yes or no : ')
else:
    print('Good bye')

