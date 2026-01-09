import requests
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self):
        self.s_response = None
        self.T_HEADERS = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        self.T_BODY = {
            'grant_type': 'client_credentials',
            'client_id': f'{CLIENT_ID}',
            'client_secret': f'{CLIENT_SECRET}',
        }
        self.token_response = None
        self._get_token()
        self.HEADERS = {
            'client_id': f'{CLIENT_ID}',
            'client_secret': f'{CLIENT_SECRET}',
            'Authorization': f'Bearer {self.token_response}'
        }

    def _get_token(self):
        self.token_response = requests.post(f'{AMADEUS_V1_URL}{TOKEN_ENDPOINT}', headers=self.T_HEADERS,
                                            data=self.T_BODY).json()['access_token']

    def iata_coder(self, city_name: dict) -> dict:
        if city_name['iataCode'] == '':
            parameters = {
                'keyword': f'{city_name['city']}'
            }
            response = requests.get(f'{AMADEUS_V1_URL}{CITIES_ENDPOINT}', headers=self.HEADERS, params=parameters)
            if len(response.json()['data'][0]['iataCode']) == 3:
                city_name['iataCode'] = response.json()['data'][0]['iataCode']
            else:
                city_name['iataCode'] = 'NOT_FOUND'
            return city_name

    def flight_search(self, destination: str) -> list:
        now = datetime.now()
        sixm_fnow = now + timedelta(10)
        BODY = {
            'originLocationCode': 'LON',
            'destinationLocationCode': destination,
            'departureDate': now.strftime('%Y-%m-%d'),
            'returnDate': sixm_fnow.strftime('%Y-%m-%d'),
            'adults': 1,
            'currencyCode': 'GBP',
        }
        s_response: requests.Response = requests.get(f'{AMADEUS_URL}{FLIGHT_SEARCH_ENDPOINT}',
                                                     headers=self.HEADERS, params=BODY)
        print(s_response.json(), s_response)
        try:
            return s_response.json()['data']
        except KeyError:
            return [{'price':{'grandTotal':'N/A'}}]

    def find_cheapest_flight(self, destination):
        flights_data: list = self.flight_search(destination)
        if flights_data[0]['price']['grandTotal'] != 'N/A':
            lower_price = flights_data[0]
            for flights in flights_data:
                print(f'price analysed: {flights['price']['grandTotal']}, against: {lower_price['price']['grandTotal']}')
                if flights["price"]['grandTotal'] < lower_price['price']['grandTotal']:
                    lower_price = flights
        else:
            lower_price = 'N/A'
        return lower_price
