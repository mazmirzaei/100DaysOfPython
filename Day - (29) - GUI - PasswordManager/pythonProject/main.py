from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    # random letter generator
    password_letters = [choice(letters) for num in range(randint(8,10))]
    password_numbers = [choice(symbols) for num in range(randint(2,4))]
    password_symbols = [choice(numbers) for num in range(randint(2,4))]
        
    # Combine all lists and shuffle them
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
        
    # Creates a string of all charactrers usinf .join insted of the for loop
    password = "".join(password_list)
    # for item in password_list:
    #     password += item
    # return password
    
    # the generated password shows inside the entry_password 
    pass_entry.insert(0, password)
    
    # make easy copy and past with CTRL+V 
    pyperclip.copy(password)

    return password

# ---------------------------- SAVE Function ------------------------------- #

def save():
    # getting input from entries
    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    
    # chekcs if some box is empty 
    if len(web) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(message="Missing some info")
    else:
        # message box
        is_ok = messagebox.askokcancel(title=web, message=f"These are the deatails entered: "
                                                          f"\nEmail:{email}"
                                                          f"\nPassword: {password} "
                                                          f"\nIs it ok to save?")
        # check entered info if all correct and save
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} | {email} | {password} \n")
                web_entry.delete(0, END)
                email_entry.delete(0, END)
                pass_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('SecurePass')
window.config(padx=20, pady=20)

# Handling img
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 102, image=logo_img)
canvas.grid(row=0, column=1)

# Create Labels
web_label = Label(text='Web Address:')
web_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

web_label = Label(text='Password:')
web_label.grid(row=3, column=0)


# Create Entry
web_entry = Entry(width=40)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()


email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "example@gamil.com")
email_entry.focus()


pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)
pass_entry.focus()
# passwords = password_generator()

# Create Buttons
pass_button = Button(text="Generate Password", command=password_generator)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()