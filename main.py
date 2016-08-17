from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


from handler import bind_events
import config as cfg

updater = Updater(token=cfg.token)

udpater = bind_events(updater)


updater.start_polling()
updater.idle()