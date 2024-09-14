import random
from hang_art import stages
from word_list import words
from hang_art import logo


#prints the logo
print(logo)

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(words)
print(chosen_word)

#Creates a list of '_' in size of the random chosen word
display = []
for n in range(0,len(chosen_word)):
    display.append('_')


#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#repalce the guess charecter in the display with '_' 

game_on = True
lives = 6

while game_on:

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess  =input('guess a letter : ').lower()
    
    if guess in chosen_word:
        for n in range(0,len(chosen_word)):
            if chosen_word[n] == guess:
                display[n] = guess      
                new_display = " ".join(display)
        print(new_display) 
        
        
    #if the guess is wrong
    else:
        lives -= 1
        print(stages[lives])

        if lives == 0:
            game_on = False
            print('You Lose. ')
            
    #If player wins the games ends here    
    if "_" not in display:
        game_on = False
        print('You Win!')
            