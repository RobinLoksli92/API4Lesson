import os
from os import listdir
from pathlib import Path
import telegram
import time
from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_some_launch
from fetch_nasa import fetch_nasa_epic_images, fetch_nasa_image_of_the_day


def download_images(images_path, spacex_launch_number, nasa_api_key):
    fetch_nasa_epic_images(images_path, nasa_api_key)
    fetch_spacex_some_launch(images_path, spacex_launch_number)
    fetch_nasa_image_of_the_day(images_path, nasa_api_key)


def send_photo_to_telegram_channel(bot, images_path,channel_chat_id):
    while True:
        for photo_path in listdir(images_path):
            with open(f'{images_path}/{photo_path}', 'rb') as space_photo:
                bot.send_photo(
                    chat_id=channel_chat_id,
                    photo=space_photo
                )
            time.sleep(24*60*60)


def main():
    load_dotenv()
    images_path = 'images'
    Path(images_path).mkdir(parents=True, exist_ok=True)
    spacex_launch_number = 60
    nasa_api_key = os.getenv('NASA_API_KEY')
    download_images(images_path, spacex_launch_number, nasa_api_key)

    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(telegram_bot_token)
    channel_chat_id = os.getenv('TELEGRAM_CHANNEL_ID')
    send_photo_to_telegram_channel(bot, images_path, channel_chat_id)
    

if __name__ == '__main__':
    main()


