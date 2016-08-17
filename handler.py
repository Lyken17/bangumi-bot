from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hello World!')


def hello(bot, update):
    bot.sendMessage(update.message.chat_id,
                    text='Hello {0}'.format(update.message.from_user.first_name))


def echo(bot, update):
    text = "【豌豆字幕組&風之聖殿字幕組】★7月新番[禁忌咒紋 / Taboo_Tattoo][07][繁體][720P][MP4][百度網盤]\n" \
           "种子地址: https://bangumi.moe/download/torrent/57b2b4b55cc0696f1ce1a6f7/%E3%80%90%E8%B1%8C%E8%B1%86%E5%AD%97%E5%B9%95%E7%B5%84%26%E9%A2%A8%E4%B9%8B%E8%81%96%E6%AE%BF%E5%AD%97%E5%B9%95%E7%B5%84%E3%80%91%E2%98%857%E6%9C%88%E6%96%B0%E7%95%AA%5B%E7%A6%81%E5%BF%8C%E5%92%92%E7%B4%8B%20_%20Taboo_Tattoo%5D%5B07%5D%5B%E7%B9%81%E9%AB%94%5D%5B720P%5D%5BMP4%5D%5B%E7%99%BE%E5%BA%A6%E7%B6%B2%E7%9B%A4%5D.torrent"
    bot.sendMessage(chat_id=update.message.chat_id, text=text)



def bind_events(updater):

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('hello', hello))

    echo_handler = MessageHandler([Filters.text], echo)
    updater.dispatcher.add_handler(echo_handler)
