# from datetime import datetime
# parameters = {
#     'lat': 32.841991,
#     'lng': -117.273018,
#     'formatted': 0,
# }
# 
# # web request
# # https://api.sunrise-sunset.org/json?lat=32.841991&lng=-117.273018
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)
# 
# # time is 24 hrs formatted
# sunrise_time = data['results']['sunrise'].split('T')[1].split(':')[0]
# sunset_time = data['results']['sunset'].split('T')[1].split(':')[0]
# print(sunrise_time,sunset_time )



# ISS Tracker Project
# this project sends email whenever the ISS satelite is over our location
import requests
import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "maztest7@gmail.com"
MY_PASSWORD = "************"
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


# get data from iss api endpoint
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    #getting position of iss sattlite
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if (MY_LAT-5) <= iss_latitude <= (MY_LAT+5) and (MY_LONG-5) <= iss_longitude <= (MY_LONG+5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # getting sunrise and sunset in 24 hrs formatted from iss api endpoint
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # current time
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("maztest7@yahoo.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )












