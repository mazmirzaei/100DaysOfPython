import requests
from datetime import datetime, timedelta
from pprint import pprint
from flight_data import FlightData

api_key = "2fqDf6-i0DV6EjOKUzY68e2MUnwYTrgb"

class FlightSearch:
    # 4
    def get_destination_code(self, city_name):
        """
        This method responsible to search and return iata code for pass in city_name
        :param city_name: gets input from google sheet
        :return: iata_code
        """
        tequila_endpoint = "https://tequila-api.kiwi.com"
        location_endpoint = f"{tequila_endpoint}/locations/query"
        headers = {"apikey": api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        result = response.json()['locations']
        iata_code = result[0]['code']
        return iata_code
    
# data = FlightSearch()
# dt = data.get_destination_code('Tehran')
# print(dt)
    
    #9
    def get_price(self, iata_origin_code, iata_dest_code):
        
        date = datetime.now() + timedelta(1)
        date_from = date.strftime("%d/%m/%Y")

        date_t = datetime.now() + timedelta(180)
        data_to = date_t.strftime("%d/%m/%Y")

        end_point = 'https://tequila-api.kiwi.com/v2/search'
        headers = {"apikey": api_key}
        query = {
            "fly_from": iata_origin_code,
            "fly_to": iata_dest_code,
            "date_from": date_from,
            "date_to": data_to,
            "flight_type": "round",
            "curr": "USD",
        }
        response = requests.get(url=end_point, headers=headers, params=query)
        data = response.json()['data'][0]
        # 11
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data

