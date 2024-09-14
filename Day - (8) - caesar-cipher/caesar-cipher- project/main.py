from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text,shift,direction):
    cipher_text =''
    for char in text:
        if char in alphabet:
            if direction == 'encode':
                cipher_text += alphabet[alphabet.index(char)+shift]
            elif direction == 'decode':
                cipher_text += alphabet[alphabet.index(char)-shift]
        else:
            print('Wrong')
        
    print(cipher_text)


#Logo
print(logo)


#ask your if they want to restart
cipher_on = True
while cipher_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #in case of user enters a shift greater than the number of letter alphabet
    shift = shift % 26
    
    #calling caesar function
    caesar(text,shift,direction)
    
    
    reset= input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if reset == 'no':
        cipher_on = False
        print('Good Bye!')
    
    
    

#another cipher function version:
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")
