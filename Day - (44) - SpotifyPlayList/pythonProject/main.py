# #Scaping billbord.com web site to scrap best 100 msic on specefic date
# 
# 
# # response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# # web_page = response.text
# #
# # soup = BeautifulSoup(web_page, "html.parser")
# # movie_title = soup.find_all(name='h3', class_="title")
# # movie_list= []
# # for title in movie_title[::-1]:
# #     text = title.getText()
# #     movie_list.append(text)
# # print(movie_list)
# #
# # with open("movie.txt", "w", encoding="utf-8") as file:
# #     for movie in movie_list:
# #         file.write(f"{movie} \n")
# 
# from bs4 import BeautifulSoup
# import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# 
# # Scraping Billboard 100
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
# web_page = response.text
# soup = BeautifulSoup(web_page, "html.parser")
# song_name = soup.find_all("span", class_="chart-element__information__song")
# song_list = [song.getText() for song in song_name]
# print(song_list)
# 
# 
# #Spotify Authentication
# Client_ID = "9971daf62a744cfcb823b4e020958052"
# Client_Secret = "118786b3b157454bb409a2821fda9c49"
# 
# spoty_autn = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=Client_ID,
#         client_secret=Client_Secret,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = spoty_autn.current_user()["id"]
# 
# #Searching Spotify for songs by title
# #Handling errors in case of of the song does't exsists
# song_uris = []
# year = date.split("-")[0]
# # print(year)
# for song in song_name:
#     result = spoty_autn.search(q=f"track:{song} year:{year}",type= "track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")
# 
# #Creating a new private playlist in Spotify
# playlist = spoty_autn.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
# 
# #Adding songs found into the new playlist
# spoty_aut.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="9971daf62a744cfcb823b4e020958052",
        client_secret="118786b3b157454bb409a2821fda9c49",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)
