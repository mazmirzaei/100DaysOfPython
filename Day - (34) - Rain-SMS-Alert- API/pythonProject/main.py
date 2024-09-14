import requests
import os
from twilio.rest import Client
import emoji

account_sid = os.environ['************************************']
auth_token = os.environ['************************************']

# api_key = "************************************"
# end_point = "https://api.openweathermap.org/data/2.5/onecall"
# https://api.openweathermap.org/data/2.5/onecall?lat=32.889780&lon=-117.253390&exclude={part}&appid=************************************
# parameters = {
#     "lat":32.889780,
#     "lon":-117.253390,
#     "api":api_key,
#     "exclude":"current,minutely,daily"
# }

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=-25.263741&lon=-57.575928&exclude=current,minutely,daily,&appid=************************************")
response.raise_for_status()
print(response.status_code)
data = response.json()

for hr in range(0, 24):
    if data['hourly'][hr]['weather'][0]['id'] < 800:
        is_rain = True

if is_rain:
    print('Bring an Umbrella')
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="Today Is Raining, Bring an Umbrella :umbrella: ",
                     from_='+12052895138',
                     to='+************'
                 )
print(message.status)
