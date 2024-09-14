# Amazon price tracking bot
# Python Bot Project, Checks constantly a 
# price of targetd item and sends notification to our email to but the item on Amazon.

import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
# print(price)

price_without_currency = price.split('$')[1]
# print(price_without_currency)

price_as_float = float(price_without_currency)
print(price_as_float)


#Email when price is below our target

import smtplib

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("maztest7@gmail.com", "********")
        connection.sendmail(
            from_addr="maztest7@gmail.com",
            to_addrs="maztest7@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )






















