"""Add music to playlist"""
import logging
from .youtube_music import utils as yt_utils
from .spotify_playlist import utils as spot_utils

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)

logger = logging.getLogger(__name__)

def add_song(update, _):
    """Add song to playlist after determining type"""
    url = update.message.text.split("/add ")[1:][0]
    logger.debug("Do we get here?")
    # Determine type of url
    if "spotify" not in url:
        msg = "This doesn't look like a spotify URL, adding the closest song I could find: "
        
        yt_details = yt_utils.get_details(url=url)
        artist = yt_details['author']
        title = yt_details['title']
        
        logger.debug("This is the artist and the title: %s, %s", artist, title)

        spotify_url = spot_utils.get_song(artist=artist, title=title)
        msg = "This looks like a youtube URL, adding the closest song I could find: " + spotify_url

        logger.debug("This is the spotify_url %s", spotify_url)

    else:
        spotify_url = url
        msg = "Added song to playlist!"

    logger.debug("We are about to add it")
    spot_utils.add_song(song=spotify_url)

    update.message.reply_text(msg)


