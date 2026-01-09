import requests
from twilio.rest import Client



# CODE
parameters = {
    'lat': MY_LAT,
    'lon': MY_LNG,
    'appid': my_api_key,
    'units': 'metric',
    'cnt': 4,
}
will_rain = False
data = requests.get('https://api.openweathermap.org/data/2.5/forecast?', params=parameters)
data.raise_for_status()
w_data_list = data.json()['list']
for items in w_data_list:
    print(items)
    if int(items['weather'][0]['id']) < 700:
        will_rain = True
if will_rain:
    print('yes')
    client = Client(account_sid, auth_token)
    message_body = '☔It will rain today☔.\n ☔Bring your umbrella☔'
    recipient = '+5533988384379'
    message = client.messages.create(
        body=message_body,
        from_=my_phone_number,
        to=recipient,
    )
    print(message.status)
else:
    print('no')
