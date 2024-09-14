
import requests
import os
from pprint import pprint

# 1 
#Sheety api end point
sheety_endpoint = "https://api.sheety.co/60e35ac3e57ca7c65b4a5abff24b2e41/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data_dest = {}
    
    def get_dest_data(self):
        sheety_response = requests.get(sheety_endpoint)
        sheety_data = sheety_response.json()
        
        self.data_dest = sheety_data['prices']
        return self.data_dest
    
    # 6 
    # updates the Google Sheet with the IATA codes that we get from flight search class
    def update_destination_codes(self):
        for city in self.data_dest:
            new_data = {
                "price":{
                    'iataCode' : city['iataCode']
                }
            }
            # 7 
            # make put request to update the google sheet
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data)
            print(response.text)
    
