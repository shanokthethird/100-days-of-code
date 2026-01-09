import requests
import os
from datetime import datetime


APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']
APP_URL = 'https://trackapi.nutritionix.com'
APP_ENDPOINT = '/v2/natural/exercise'


headers = {
    'x-app-id':APP_ID,
    'x-app-key':APP_KEY,

}

parameters = {
    'query':input('What exercise did you do today?'),
    'weight_kg': 84,
    'height_cm': 187,
    'age': 25,
}

response = requests.post(f'{APP_URL}{APP_ENDPOINT}', headers=headers, json=parameters)
print(response.json())
duration_min = response.json()['exercises'][0]['duration_min']
duration_h=duration_min//60.
duration_m=duration_min%60
calories = response.json()['exercises'][0]['nf_calories']
exercise = response.json()['exercises'][0]['name']

sheety_url = 'https://api.sheety.co/63654c41cf5ce095cc1545c192b2f7f3/workoutTracking/workouts'
AUTH_TOKEN = os.environ['AUTH_TOKEN']

headers = {
    'Authorization': AUTH_TOKEN,
}
today = datetime.now()
sheet_data = {
    'workout': {
        'date': today.strftime('%d/%m/%Y'),
        'time': today.strftime('%H:%M:%S'),
        'exercise': exercise.title(),
        'duration': f'{int(duration_h)}h{duration_m}m',
        'calories': f'{calories}',
                   }
              }
response = requests.post(sheety_url, json=sheet_data, headers=headers)

# response = requests.get(sheety_url,headers=headers)
print(response.json())