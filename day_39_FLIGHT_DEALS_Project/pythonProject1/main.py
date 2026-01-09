from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
write_response = None
data = DataManager()
sheet_data = data.sheet_data()
lowest_price = None
low_price_list = {}

search = FlightSearch()
for items in sheet_data:
    search.iata_coder(items)

for items in sheet_data:
    write_response = data.write_data(items)

for items in sheet_data:
    lowest_price = search.find_cheapest_flight(items['iataCode'])
    low_price_list.update()

send_msg = NotificationManager(low_price_list)
send_msg.send_msg()
