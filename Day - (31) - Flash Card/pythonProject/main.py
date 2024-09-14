from images import *
from tkinter import *
import random
import pandas as pd

######################## Constants  #######################
BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
word_list={}

###################### Read, update Data ########################
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    print(original_data)
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")

##################### Remove a card ####################
def remove_card():
   word_list.remove(random_word)
   data = pd.DataFrame(word_list)
   data.to_csv('data/word_to_lern.csv', index=False)
   next_card()

####################### next card ######################
def next_card():
   global random_word, flip_timer
   window.after_cancel(flip_timer)
   random_word = random.choice(word_list)
   canvas.itemconfig(card_title, text = 'French', fill='black')
   canvas.itemconfig(card_word, text=random_word['French'], fill='black')
   canvas.itemconfig(card_background, image=card_front)
   flip_timer = window.after(3000, func=flip_card)


###################### flip card #######################
def flip_card():
   canvas.itemconfig(card_title, text='English', fill='white')
   canvas.itemconfig(card_word, text=random_word['English'], fill='white')
   canvas.itemconfig(card_background, image= card_back)
   
   
##################### UI Setup ##########################
window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# after 3s the dard flip and diplay English translation for the current word
flip_timer = window.after(3000, func=flip_card)

# cards
canvas = Canvas(height =650, width=800, bg= BACKGROUND_COLOR, highlightthickness=0 )
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background  = canvas.create_image(400, 290, image=card_front)
card_title = canvas.create_text(400,150, text="", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400,300, text="", font=("Ariel", 60, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)
# call next_card() function, shows the first card when program runs



# buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command = remove_card)
right_button.grid(row=1, column=0, )

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command = next_card)
wrong_button.grid(row=1, column=1)

next_card()
window.mainloop()

