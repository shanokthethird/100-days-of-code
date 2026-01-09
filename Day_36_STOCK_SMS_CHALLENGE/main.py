import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# odd_months = [1, 3, 5, 7, 9, 11]
# even_months = [2, 4, 6, 8, 10, 12]
#
#
# alpha_parameters = {
#     'function': 'TIME_SERIES_DAILY',
#     'symbol': STOCK,
#     'apikey': ALPHA_API_KEY,
# }
# yesterday = ''
# alpha_data = requests.get('https://www.alphavantage.co/query?', params=alpha_parameters).json()
# last_date = alpha_data['Meta Data']['3. Last Refreshed'].split('-')
# today = f'{last_date[0]}-{last_date[1]}-{last_date[2]}'
# if int(last_date[1]) == 1:
#     yesterday = f'{last_date[0]}-0{int(last_date[1])-1}-{31}'
# elif int(last_date[1]) == 3:
#     yesterday = f'{last_date[0]}-0{int(last_date[1])-1}-{29}'
# elif int(last_date[1]) in odd_months and int(last_date[2]) == 1:
#     yesterday = f'{last_date[0]}-0{int(last_date[1])-1}-{30}'
# elif int(last_date[1]) in even_months and int(last_date[2]) == 1:
#     yesterday = f'{last_date[0]}-0{int(last_date[1])-1}-{31}'
# else:
#     yesterday = f'{last_date[0]}-0{int(last_date[1])}-{int(last_date[2])-1}'
# close_value_today = float(alpha_data["Time Series (Daily)"][today]['4. close'])
# close_value_yesterday = float(alpha_data["Time Series (Daily)"][yesterday]['4. close'])
# percentage_diff = (close_value_today-close_value_yesterday)/close_value_yesterday
#
# if percentage_diff > 0.05 or percentage_diff < -0.05:
#     print('GET NEWS')


# # # STEP 2: Use https://newsapi.org
# # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


NEWS_API_KEY = 'ebff269d4495484fba5281992d10a8de'
news_parameters = {
    'apikey': NEWS_API_KEY,
    'q': COMPANY_NAME,
    'from': '2024-07-25',
    'to': '2024-07-26',
    'sortBy': 'relevancy',
    'pageSize': 3,
}
news_data = requests.get('https://newsapi.org/v2/everything?', params=news_parameters).json()['articles']
article_titles = []
article_contents = []
for article in news_data:
    article_titles.append(article['title'])
    article_contents.append(article['description'])
print(f'{article_titles}\n\n\n {article_contents}')


# # STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


message = client.messages.create(
    body=f"\n{STOCK}: 🔺{percentage_diff*100}%,\n\n Headline:{article_titles[0]}\nBrief:{article_contents[0]}\n\n\n"
         f"Headline:{article_titles[1]}\nBrief:{article_contents[1]}\n\n\n Headline:{article_titles[2]}\nBrief:{article_contents[2]}",
    from_=my_phone_number,
    to="+5533988384379",
)
message.Status()

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file 
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""
    