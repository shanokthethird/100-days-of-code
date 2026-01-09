import datetime as dt
import pandas as pd
from random import randint
import smtplib

URL_EMAIL = 'smtp.gmail.com'
MY_EMAIL = 'xxshanok3xx@gmail.com'
PASSWORD = 'zizb qfxw igpn fhsp'

data = pd.read_csv('birthdays.csv')

today = (dt.datetime.now().month, dt.datetime.now().day)
birthdays_dict = {(data_row['month'],data_row['day']): data_row for (index,data_row) in data.iterrows()}

if today in birthdays_dict:
    file_path = f'letter_templates/letter_{randint(1,3)}'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_content = contents.replace('[NOME]', birthdays_dict[today]['name'])
        with smtplib.SMTP(URL_EMAIL) as connection:
            connection.starttls()
            connection.login(
                user=MY_EMAIL,
                password=PASSWORD
            )
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=f'{birthdays_dict[today]['email']}',
                msg=f'Subject: HAPPY BIRTHDAY\n\n{new_content}'
            )
