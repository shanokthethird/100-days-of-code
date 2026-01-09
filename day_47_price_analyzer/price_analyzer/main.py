import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://appbrewery.github.io/instant_pot/'
resp = requests.get(url=URL)

soup = BeautifulSoup(resp.text, 'html.parser')

price = soup.select('div div div div div div div div div div div span span span')
price = f'${price[1].text.strip('.')}.{price[3].text}'
print(price)
