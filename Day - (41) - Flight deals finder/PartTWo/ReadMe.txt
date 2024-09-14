In the Seconed part of the Project we use replit.com to host our code and share the link to the console with our user. 

1- Create a new Repl.it project.
2- Create a new Sheet (Tab) in your Copy of Flight Deals Google and Add 3 new column headings - "First Name", "Last Name", "Email" to this new user Sheet.
3- Sync the new sheet in Sheety.
4- Enable the POST method in the users endpoint
5- Code up the Repl.it project so that it asks the user for their first name, last name and email. 
6- Use the Sheety API to POST the data that the user enters into the user sheet in your Copy of Flight Deals Google Sheet.

Errors Handling:

Exception Handling for Destinations without Flights
- use try/except/else to catch the situations when the flight data is empty and let the code continue without crashing.

Destinations without Direct Flights
 - If a flight is not found, check to see if there are flights with 1 stop and pretty print the result with pprint().


 Last step : Email all our customers
 notify our customers when there is a good deal!
 Use smtplib and sending emails to send all our customers in the users sheet from Google Sheets the message that contains the flight deal.