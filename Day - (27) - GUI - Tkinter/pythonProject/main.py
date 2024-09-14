import tkinter
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=('Arial', 24, 'bold'))
my_label.grid(row=0, column=0)
my_label.config(padx=20, pady=20)

# update and config the privious value for txt
my_label['text'] = 'new text'
my_label.config(text='New text')

# Button
def button_clicked():
    print('Hello')
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text='Clik me', command=button_clicked)
#all centerd by defult
# button.pack() # side='right'
# button.place(x=100, y=100)
button.grid(row=0, column=2)
# button.config(padx=20, pady=20)

# Entry
input = tkinter.Entry(width = 10)
input.grid(row=0, column=3)







window.mainloop()
