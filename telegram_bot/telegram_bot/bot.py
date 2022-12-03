"""Main bot that has the features"""
import os
from telegram.ext import Updater, CommandHandler

from telegram_bot.logger import logger
from telegram_bot.features import handlers

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", None)
APP_NAME = os.environ.get("APP_NAME", None)
BOT_PORT = int(os.environ.get("BOT_PORT", 8443))



class MisterRoboto:
    """The Robot himself"""

    def __init__(self):
        self.name = "MisterRoboto"

    def main(self):
        """Starts the bot."""
        updater = Updater(TELEGRAM_TOKEN, use_context=True)

        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher
        help_text = "The following commands are available:\n"
        for cmd, handler, help_txt in handlers:
            dispatcher.add_handler(CommandHandler(cmd, handler))
            help_text += cmd + ": " + help_txt + "\n"

        def help_handler(update, _):
            """Sends a message when the command /help is issued."""
            logger.debug("Calling helper")
            update.message.reply_text(help_text)

        def error(update, context):
            """Log Errors caused by Updates."""
            logger.warning('Update "%s" caused error "%s"', update, context.error)


        dispatcher.add_handler(CommandHandler("help", help_handler))
        dispatcher.add_error_handler(error)


        updater.start_webhook(
            listen="0.0.0.0",
            port=BOT_PORT,
            url_path=TELEGRAM_TOKEN,
            webhook_url=APP_NAME + TELEGRAM_TOKEN,
        )
        logger.debug("We are about to idle")
        updater.idle()
