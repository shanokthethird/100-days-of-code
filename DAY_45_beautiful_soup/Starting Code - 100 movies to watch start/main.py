import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

resp = requests.get(URL)

soup = BeautifulSoup(resp.text, 'html.parser')

h3_head = soup.find_all('h3')

with open('bestMovies.txt', 'a') as file:
    for title in h3_head:
        file.write(f'{title.getText()}\n')


# Write your code below this line 👇


