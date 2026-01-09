import requests
import os
from dotenv import load_dotenv

SHEETY_URL = 'https://api.sheety.co/63654c41cf5ce095cc1545c192b2f7f3/flightDeals/prices'



# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.sheets_data = None
        self.put_response = None
        self.response = requests.get(SHEETY_URL, headers=HEADERS)

    def sheet_data(self):
        return self.response.json()['prices']

    def write_data(self, sheets: dict):
        self.put_response = requests.put(f'{SHEETY_URL}/{int(sheets['id'])}', json={'price': sheets}, headers=HEADERS)
        return self.put_response

    def read_data(self):
        self.sheets_data = requests.get(f'{SHEETY_URL}', headers=HEADERS)
        return self.sheets_data
