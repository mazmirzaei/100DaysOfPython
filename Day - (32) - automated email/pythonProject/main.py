import datetime as dt
import random
import smtplib

my_email = "maztest7@gmail.com"
password = "*************"

now = dt.datetime.now()
current_day = now.weekday()

if current_day == 5:
    with open("quotes.txt", "r") as file:
        lines = file.readlines()
        quote = random.choice(lines)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        # to secure the email encrypted and it is impossible to read the email content
        # makes connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs='maztest7@yahoo.com',
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
