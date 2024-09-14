import requests
from pprint import pprint
from data_manager import DataManager

#13
from notification_manager import NotificationManager
notification_manager = NotificationManager()

# 4 
from flight_search import FlightSearch
flight_search = FlightSearch()

# 2
# gets data from google sheet
data_manager = DataManager()
sheet_data = data_manager.get_dest_data()

# 3
# if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.

# 3
if sheet_data[0]['iataCode'] == "":
    # 5
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row["city"])
    # 8
    data_manager.data_dest = sheet_data
    data_manager.update_destination_codes()
    
# 12
ORIGIN_CITY = "LAX"
for dest in sheet_data:
    flight = flight_search.get_price(
        ORIGIN_CITY,
        dest['iataCode'],
    )
    
    #13
    # for each dest in google sheet check if the price have been 
    # found is lower then the price in google sheet 
    # than send a notification to our phone
     if dest['lowestPrice'] >=  flight.price:
         notification_manager.send_sms(
             message=f"Low price alert! Only $ {flight.price} "
                     f"to fly from {flight.origin_city}-{flight.origin_airport} "
                     f"to {flight.destination_city}-{flight.destination_airport}, "
                     f"from {flight.out_date} to {flight.return_date}."
         )
 
         
    


