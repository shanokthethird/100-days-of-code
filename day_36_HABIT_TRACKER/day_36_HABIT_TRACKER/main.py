import requests
from datetime import datetime




tday = datetime(year=2024,month=7,day=29)
pixela_url = f'https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{tday.strftime('%Y%m%d')}'

# parameters = {
#     'date': tday.strftime('%Y%m%d'),
#     'quantity': '5',
# }

#MAKING A GRAPH IN PIXELA
# parameters = {
#     'name': 'Cycling Graph',
#     'unit': 'Km',
#     'type': 'float',
#     'color': 'ajisai',
# }

headers = {
    'X-USER-TOKEN': TOKEN,
}
# #SETTING UP PIXELA USER
# parameters = {
#     'token': 'Ma!@978465',
#     'username': 'shanok3',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }

# response = requests.post(url=pixela_url, json=parameters)
response = requests.delete(url=pixela_url, headers=headers)
print(response.text)
