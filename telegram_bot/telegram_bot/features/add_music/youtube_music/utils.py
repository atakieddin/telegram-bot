"""Handlers file for turning Youtube Music to Spotify"""
from urllib.parse import urlparse, parse_qs
from ytmusicapi import YTMusic


ytmusic = YTMusic()

def get_details(url):
    """Get the details of a youtube music link"""
    url_data = urlparse(url)
    query = parse_qs(url_data.query)
    video_id = query["v"][0]

    return ytmusic.get_song(video_id)['videoDetails']

    
