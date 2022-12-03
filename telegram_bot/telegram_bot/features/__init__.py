"""Collection of hander feature"""
from telegram_bot.features.add_music.handlers import add_song, show_playlist, random_song

handlers = [
    # ( cmd, handler, help)
    ("add", add_song, "Add songs to Spotify playlist"),
    ("show", show_playlist, "Show the current playlist"),
    ("random", random_song, "Pick random song from playlist")
]
