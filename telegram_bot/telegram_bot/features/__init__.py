"""Collection of hander feature"""
from .add_to_playlist.handlers import add_song

handlers = [
    # ( cmd, handler, help)
    ("add", add_song, "Add songs to Spotify Playlist"),
]
