import requests
from datetime import datetime
import os

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    'x-app-id': "88888888888",
    "x-app-key": "69htff3eht7d5her73chert36a29898989354e6d5b18tyr4e1c78542",
    "x-remote-user-id": "0",
}
user_input = input("Tell me which exercises you did?")

parameters = {
    "query": user_input,
    "gender": 'male',
    "weight_kg": "100",
    "height_cm": '178',
    "age": '35',
}

response = requests.post(url=end_point, headers=headers, json=parameters)
result = response.text
print(result)

###################### sheety part ###########################


sheety_endpiont = os.environ["https://api.sheety.co/4je826e6erb95ht458hteh2cf35bertwrtywrtdd9cec1ce072/workoutsTracking/workouts"]
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response = requests.post(sheety_endpiont, json=sheet_inputs)

# Basic Auth
sheet_response = requests.post(
    sheety_endpiont,
    json=sheet_inputs,
    auth=(
        os.environ["USERNAME"],
        os.environ["PASSWORD"],
    )
)

# Bearer Token
bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}
sheet_response = requests.post(
    sheety_endpiont,
    json=sheet_inputs,
    headers=bearer_headers
)
print(sheet_response.text)
