import os
from os import listdir
from pathlib import Path
import telegram
import time
from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_last_launch
from fetch_nasa import fetch_nasa_epic_images, fetch_nasa_image_of_the_day


def download_images(path_for_images):
    fetch_nasa_epic_images(path_for_images)
    fetch_spacex_last_launch(path_for_images)
    fetch_nasa_image_of_the_day(path_for_images)


def send_photo_to_telegram_channel(bot, path_for_images):
    chat_id = os.getenv('TELEGRAM_CHANNEL_ID')

    while True:
        for path_for_photo in listdir(path_for_images):
            with open(f'images/{path_for_photo}', 'rb') as space_photo:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=space_photo
                )
            time.sleep(24*60*60)


def main():
    Path('images').mkdir(parents=True, exist_ok=True)
    path_for_images = 'images'

    download_images(path_for_images)

    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(telegram_bot_token)
    send_photo_to_telegram_channel(bot, path_for_images)
    

if __name__ == '__main__':
    main()


