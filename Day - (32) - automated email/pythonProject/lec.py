# import smtplib 
# 
# my_email = "maztest7@gmail.com"
# password = "Maz13612wsx"
# 
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # to secure the email encrypted and it is impossible to read the email content
#     # makes connection secure
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs='maztest7@yahoo.com',
#         msg="Subject:Hello\n\nThis is the body of my email"
#     )
# 

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# day = now.day
# month = now.month
# print(day, month, year)
# 
# day_of_week = now.weekday()
# print(day_of_week)
# 
# date_of_birth = dt.datetime(day=23, month=12, year=1982)
# print(date_of_birth)
# 
# # eMAIL APPLICARION
