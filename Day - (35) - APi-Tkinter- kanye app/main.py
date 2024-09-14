# import requests
# 
# # get function helps to get data from the endpoint
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# 
# 
# # Handling diffrent respose: 
# # 1XX hold on, 
# # 2XX Sucsessful, 
# # 3XX You are not athrusied, 
# # 4XX something you looking for does not exists Client side
# # 5XX error of the server side, server down, web down
# # https://httpstatuses.com/
# response.raise_for_status()
# 
# # geting actual data using json()
# data = response.json()
# print(data)
# 
# data = response.json()["iss_position"]
# print(data)
# 
# data = response.json()["iss_position"]["longitude"]
# print(data)
# 
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (longitude,latitude)
# print(iss_position)

import requests



def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)
    




from tkinter import *
windows = Tk()
windows.title('Kanye Says...')
windows.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
bg_img = PhotoImage(file='background.png')
canvas.create_image(150,207, image=bg_img)
quote_text = canvas.create_text(150, 207, text="Hi, Push my face..", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


windows.mainloop()
















