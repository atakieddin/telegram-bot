"""Handlers file for Spotify Playlist interaction"""
import os
import json
import logging
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import MemoryCacheHandler

# Enables logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
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


def add_song(update, _):
    """Handler for adding songs"""
    song = update.message.text.split("/add ")[1:]
    spotify.playlist_add_items(os.environ["PLAYLIST_ID"], song)
    update.message.reply_text("Added song to playlist!")

def show_playlist(update, _):
    """Handler for shwoing the playlist"""
    playlist = "https://open.spotify.com/playlist/3ptj0dQmLvYYgMf81A19kl?si=48b5ad8268e1435f"
    update.message.reply_text("This is the playlist: " + playlist)

def random_song(update, _):
    """Handler for picking a random song"""
    msgs = [
        "Why not listen to %s!",
        "Give %s a try!",
        "The oracle suggests %s",
        "All signs point to %s",
        "There's only one choice: %s",
        "Let's go with %s",
        "I flipped a 500 sided coin, and this was chosen: %s",
        "If you ask me: %s",
        "I don't know, how about %s",
        "%s"
    ]
    limit = update.message.text.split("/random_song ")[1:]
    playlist_songs = spotify.playlist_items(os.environ["PLAYLIST_ID"], limit)
    song = random.choice(playlist_songs)
    msg = random.choice(msgs)
    update.message.reply_text(msg % song)