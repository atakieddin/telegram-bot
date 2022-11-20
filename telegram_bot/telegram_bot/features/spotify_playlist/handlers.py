"""Handlers file for Spotify Playlist interaction"""
import os
import json
import logging
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import MemoryCacheHandler

# Enables logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
SCOPE = "playlist-modify-private playlist-modify-public"
FILEPATH = os.path.dirname(__file__)
FILENAME = "/secret_spotify_token.json"
with open(FILEPATH + FILENAME, encoding="utf-8") as spot_token:
    token_info = json.load(spot_token)

token = SpotifyOAuth(
    scope=SCOPE,
    show_dialog=False,
    cache_handler=MemoryCacheHandler(token_info=token_info),
)
spotify = spotipy.Spotify(auth_manager=token, requests_timeout=15, retries=10)


def add_song(update, _):
    """Handler for adding songs"""
    song = update.message.text.split("/add ")[1:]
    spotify.playlist_add_items(os.environ["PLAYLIST_ID"], song)
    update.message.reply_text("Added song to playlist!")
