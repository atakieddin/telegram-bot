"""Handlers file for Spotify Playlist interaction"""
import os
import json
import random
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

def show_playlist(update):
    """Handler for shwoing the playlist"""
    playlist = "https://open.spotify.com/playlist/3ptj0dQmLvYYgMf81A19kl?si=48b5ad8268e1435f"
    update.message.reply_text("This is the playlist: " + playlist)

def random_song(update):
    """Handler for picking a random song"""
    msgs = [
        "Why not listen to %s -- %s!",
        "Give %s a try! -- %s",
        "The oracle suggests %s - %s",
        "All signs point to %s -- %s",
        "There's only one choice: %s -- %s",
        "Let's go with %s -- %s",
        "I flipped a 500 sided coin, and this was chosen: %s -- %s",
        "If you ask me: %s -- %s",
        "I don't know, how about %s -- %s",
        "%s -- %s"
    ]
    limit = update.message.text.split("/random ")[1:]
    playlist_songs = [
        (
            song_info["track"]["name"],
            song_info["track"]["external_urls"]["spotify"]
        )
        for song_info in spotify.playlist_items("3ptj0dQmLvYYgMf81A19kl", limit=limit)["items"]
    ]
    song, link = random.choice(playlist_songs)
    msg = random.choice(msgs)
    update.message.reply_text(msg % (song, link))