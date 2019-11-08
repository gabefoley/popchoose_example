import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_KEY = "84c843df085a4a75b0dab8be510d6766"
SPOTIFY_SECRET = "905ccc020cac42e980ff4b2a704d9d52"

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_KEY, client_secret=SPOTIFY_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
