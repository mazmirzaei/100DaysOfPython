
import tkinter 


window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

# labels
label_one = tkinter.Label(text="is equal to : ")
label_one.grid(row=1, column=0)

label_two = tkinter.Label(text="Miles")
label_two.grid(row=0, column=2)

label_three = tkinter.Label(text="Km")
label_three.grid(row=1, column=2)

km_out = tkinter.Label(width=8)
km_out.grid(row=1, column=1)

# Entry
entry_mile = tkinter.Entry(width=8)
entry_mile.grid(row=0, column= 1)



# button
def calculate():
    mile = float(entry_mile.get())
    km = round(mile * 1.6)
    km_out.config(text=f"{km}")
    
    
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)



window.mainloop()