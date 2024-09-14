import random
import pandas as pd
import datetime as dt
import smtplib

#email info
my_email = "maztest7@gmail.com"
password = "************"

# create a tuple of month and day for current date
today = dt.datetime.now()
current_date = (today.month, today.day)
print(current_date)

# read the csv file as a pandas data frame
df = pd.read_csv('birthdays.csv')

# dictionary comprension for the frame work
birth_dictionary = {(df_row['month'], df_row['day']): df_row for (index, df_row) in df.iterrows()}

# check if month, day is in dic
if (today.month, today.day) in birth_dictionary:
    # get access to df_row 
    birth_person = birth_dictionary[current_date]#(month,day)
    # get random path file 
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # opens a random letter and replace [name} with a person
    with open(file_path) as file_letter:
        content = file_letter.read()
        content = content.replace('[NAME]', birth_person['name'])
    # sending email to the person that birth date mached
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs='maztest7@yahoo.com',
            msg=f"Subject:Happy BirthDay\n\n{content}"
        )
        
        
    




