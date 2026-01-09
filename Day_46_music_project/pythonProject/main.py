import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth



SCOPE = "playlist-read-private playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
                                               client_secret=YOUR_APP_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope=SCOPE))

# print(results)



date = input('Welcome to time travel machine. What date do you want to go back to(YYYY-MM-DD)?')
URL = f'https://www.billboard.com/charts/hot-100/{date}/'

resp = requests.get(URL)
playlist_name=f'Billboard 100 {date}'
results = sp.user_playlist_create('31zwgqhleavhr653hzgpcyinmou4',playlist_name,False)


soup = BeautifulSoup(resp.text, 'html.parser')

h3_heads = soup.select('li ul li h3')
best_list = []
num = soup.select('ul li span')



# for x in range(len(h3_heads)):
#     best_list.append([h3_heads[x].getText(), num[x].get_text()])

titles = [item.getText().strip() for item in h3_heads]
nums = [item.getText() for item in num]
control = 1
current_playlists = sp.current_user_playlists()
id_titles = []
for title in titles:
    searched_title = sp.search(f'track:{title} year:{date.split('-')[0]}')
    print(f'adding {control}) {title} to playlist')
    control += 1
    # print(searched_title)
    # id_titles.append(searched_title['tracks']['items'][0]['uri'])
    if len(searched_title['tracks']['items'])>0:
        sp.playlist_add_items(current_playlists['items'][0]['id'], [searched_title['tracks']['items'][0]['uri']])
    else:
        pass



# sp.playlist_add_items(current_playlists['items'][0]['id'],titles,)

# print(titles)
# print(best_list)