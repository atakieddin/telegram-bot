"""Handlers file for Spotify Playlist interaction"""
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import MemoryCacheHandler


SCOPE = "playlist-modify-private playlist-modify-public"
FILEPATH = os.path.dirname(__file__) if not os.environ.get("RENDER", 0) else "/etc/secrets/"
FILENAME = "/secret_spotify_token.json"

with open(FILEPATH + FILENAME, encoding="utf-8") as spot_token:
    token_info = json.load(spot_token)

token = SpotifyOAuth(
    scope=SCOPE,
    show_dialog=False,
    cache_handler=MemoryCacheHandler(token_info=token_info),
)
spotify = spotipy.Spotify(auth_manager=token, requests_timeout=15, retries=10)


def get_song(artist, title):
    """Handler for getting song"""
    results = spotify.search(q='artist:' + artist + " track:" + title, type='track')
    spotify_url = results['tracks']['items'][0]['external_urls']['spotify']
    return spotify_url

def add_song(song):
    """Add a song to the spotify playlist"""
    spotify.playlist_add_items(os.environ["PLAYLIST_ID"], [song])