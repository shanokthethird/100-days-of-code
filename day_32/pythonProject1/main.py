# import smtplib
# import datetime as dt
# from random import choice
#
# with open('quotes.txt') as quotes:
#     quotes_list = quotes.readlines()
#     print(quotes_list)
# rand_quote = choice(quotes_list)
#
# now = dt.datetime.now()
# MONDAY = 0
#
# if dt.datetime.now().weekday() == MONDAY:
#     URL_EMAIL = 'smtp.gmail.com'
#     my_email = 'xxshanok3xx@gmail.com'
#     password = 'zizb qfxw igpn fhsp'
#
#     with smtplib.SMTP(URL_EMAIL) as connection:
#         connection.starttls()
#         connection.login(
#             user=my_email,
#             password=password
#         )
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs='matheuspvds@gmail.com',
#             msg=f'Subject: GOOD MONDAY.\n\n{rand_quote}'
#         )


##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
from random import choice
import pandas

URL_EMAIL = 'smtp.gmail.com'
my_email = 'xxshanok3xx@gmail.com'
password = 'zizb qfxw igpn fhsp'
letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']
char_index = 6
letter = ''
# 1. Update the birthdays.csv
bday_dict = pandas.read_csv(
    'birthdays.csv'
).to_dict(
    # orient='tight',
    index='False'
)
print(bday_dict)

# 2. Check if today matches a birthday in the birthdays.csv
td = dt.datetime.now()
months = list(bday_dict['month'].values())
day = list(bday_dict['day'].values())
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
with open(choice(letters)) as letter_file:
    letter_rl = letter_file.read()
for key in months:
    for days in day:
        if key == td.month and days == td.day:
            global ind
            ind = months.index(key)
with smtplib.SMTP(URL_EMAIL) as connection:
    connection.starttls()
    connection.login(
        user=my_email,
        password=password
    )
    connection.sendmail(
        from_addr=my_email,
        to_addrs=f'{bday_dict['email'][ind]}',
        msg=f'Subject: HAPPY BIRTHDAY\n\n{letter.replace('[NOME]', bday_dict['name'][ind])}'
    )

# 4. Send the letter generated in step 3 to that person's email address.


# if dt.datetime.now().weekday() == MONDAY:

#
