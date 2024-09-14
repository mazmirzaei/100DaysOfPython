This application finds the cheapest flight for the provided trgets.
1- Here's how my program works. First, we have a Google sheet which keeps track of the locations that we want to visit and a price cutoff. So a historical low price. So we take this data from our Google sheet with lots of different locations and their lowest prices.

2- And we feed that into a flight search API, which is going to run every day, searching through all of the locations looking for the cheapest flight in the next six months. When it comes up with a hit and it finds a flight that's actually cheaper than our predefined price, then it's going to send that date and price via our Twilio SMS module to our mobile phone so that we can book it right there and then. 

Workflow: google sheet > flight API > SMS
 Technologies used in project: 
 	- Google Sheet
 	- APIs Required:
 			- Google Sheet Data Management - https://sheety.co/
 			- Flight Search API - https://partners.kiwi.com/
 			- Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api
 			- Twilio SMS API - https://www.twilio.com/docs/sms
 			- IATA airport code
 	- Python 3
 	- Pycharm IDE
