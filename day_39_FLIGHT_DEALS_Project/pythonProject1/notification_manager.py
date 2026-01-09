import requests
from twilio.rest import Client



class NotificationManager:
    def __init__(self, low_price_list: list):
        if len(low_price_list) == 0:
            self.msg = 'There are no flights available'
        else:
            self.msg = (f'Low price alert! Only '
                        f'{low_price_list['price']['grandTotal']} to fly from '
                        f'{low_price_list[0]['itineraries'][0]['departure']['iataCode']} to '
                        f'{low_price_list[0]['itineraries'][0]['arrival']['iataCode']}, on '
                        f'{low_price_list[0]['itineraries'][0]['departure']['at']} until '
                        f'{low_price_list[0]['itineraries'][0]['arrival']['at']}')
        #This class is responsible for sending notifications with the deal flight details.

    def send_msg(self):
        message = client.messages.create(
            body=self.msg,
            from_=my_phone_number,
            to="+5533988384379",
        )
        message.Status()
