import time
import requests
import datetime as dt
from math import floor
import smtplib

MY_LAT = -18.867789
MY_LNG = -41.966153
URL_EMAIL = 'smtp.gmail.com'
MY_EMAIL = 'xxshanok3xx@gmail.com'
APP_PASSWORD = 'zizb qfxw igpn fhsp'


def iss_pos_is_true():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    long_data = float(response.json()['iss_position']['longitude'])
    lat_data = float(response.json()['iss_position']['latitude'])
    iss_pos = (long_data, lat_data)
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LNG - 5 <= long_data <= MY_LNG + 5 and MY_LAT - 5 <= lat_data <= MY_LAT + 5:
        return True
    else:
        return False

def dark_or_light():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }
    response = requests.get(f'https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    hour_now = dt.datetime.now().hour
    if hour_now <= sunrise or hour_now >= sunset:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if iss_pos_is_true() and dark_or_light():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(
                user=MY_EMAIL,
                password=APP_PASSWORD,

            )
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="SUBJECT: LOOK UP\n\n The ISS is in your sky's viewing scope",
            )


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

#Response Codes:
#1xx: Hold on
#2xx: Here you go
#3xx: Go away
#4xx: You screwed up
#5xx: I screwed up (the server)
