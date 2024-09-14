import requests
from newsapi import NewsApiClient
from datetime import datetime
from twilio.rest import Client

##################################### stock API ####################################################
STOCK_NAME = "TSLA"
STOCK_key = "AC9LCSZ2ZCIPF2Q9"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_parameters = {
    'function': "TIME_SERIES_DAILY_ADJUSTED",
    'symbol': "TSLA",
    'interval': '5min',
    'apikey': STOCK_key,
}
response_stock = requests.get(STOCK_ENDPOINT, params= STOCK_parameters)
response_stock.raise_for_status()
stock_data = response_stock.json()["Time Series (Daily)"]

# Get yesterday's closing stock price. 
yesterday_closing_price = [info['4. close'] for (date, info) in stock_data.items()][1]
p2 = float(yesterday_closing_price)

# Get the day before yesterday's closing stock price
before_yesterday_closing_price = [info['4. close'] for (date, info) in stock_data.items()][2]
p1 = float((before_yesterday_closing_price))

#  difference between yesterday_closing_price and before_yesterday_closing_price.
difference = round((p1-p2),2)
up_down = None
if difference > 0 :
    up_down = "🔺"
else:
    up_down = "🔻"
    
# Calculate percentage change
percentage_change = ((p2-p1)/abs(p1)) * 100



################################################### news API ###################################################
# if diffrence percentage is grater than 5 use the News API to get articles related to the COMPANY_NAME.
# percentage is greater than 5 then get news
if abs(percentage_change) > 2 :
    NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"
    NEWS_API_KEY = "ce0cd94e22024461954a1e0938f91e2c"
    NEWS_parameters = {
        'apiKey': NEWS_API_KEY,
        'q': 'Tesla inc',
    }
    response_news = requests.get(NEWS_ENDPOINT, params=NEWS_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()['articles']
    
    # three recent news
    latest_news = news_data[:3]
    print(latest_news)
    
    # the first 3 article's headline and description using list comprehension.
    articles = [f"{STOCK_NAME}: {up_down}{percentage_change}% \nHeadline : {line['title']} \nBrief: {line['description']}" for line in latest_news]
    
    print(articles)
    
    # Useing twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to a phone number. 
    # Sends each article as a separate message via Twilio. 
    client = Client(account_sid, auth_token)
    for article in articles:
        message = client.messages \
            .create(
            body=article,
            from_='+12052895138',
            to='+************'
        )
    print(message.status)
    
# sapmle SMS
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

