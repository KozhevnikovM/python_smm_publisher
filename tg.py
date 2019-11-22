import telegram
from config import TG_BOT_TOKEN


def tg_send_to_chanel(chanel, message=None, photo=None):
    bot = telegram.Bot(token=TG_BOT_TOKEN)
    caption = message if message else None
    if not photo:
        return bot.send_message(chanel, text=message)
    return bot.send_photo(chanel, photo=open(photo, 'rb'), caption=caption)


if __name__ == '__main__':
    pass