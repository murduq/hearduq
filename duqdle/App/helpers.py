import random, webbrowser
import spotipy as spy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from datetime import date
import requests

def gen_song():
    scope = "user-library-read"

    # sp = spy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    with open('tokenfile') as file:
        client_id, client_secret, redir = file.read().splitlines()
    sp = spy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, 
                                                client_secret=client_secret,
                                                redirect_uri=redir))

    playlists = sp.user_playlists('spotify')
    playlist = random.choice(playlists['items'])
    playlist = playlists['items'][0]
    print(f"Selected playlist is: {playlist['name']}")
    
    random.seed(str(date.today()))
    songlist = sp.playlist(playlist_id=playlist['id'])['tracks']['items']
    song = random.choice(songlist)
    print(f"Selected song is: {song['track']['name']} - {song['track']['artists'][0]['name']}")
    
    song_dict = {}
    song_dict['title'] = song['track']['name']
    song_dict['artist'] = song['track']['artists'][0]['name']
    img_data = requests.get(song['track']['album']['images'][0]['url']).content
    with open('media/album_art.jpg', 'wb') as handler:
        handler.write(img_data)
    song_dict['image'] = song['track']['album']['images'][0]['url']
    song_dict['audio_file'] = 'test.mp3'
    # audio_link = 
    # duration = 
    return song_dict
    
if __name__ == '__main__':
    gen_song()