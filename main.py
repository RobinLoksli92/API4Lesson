import os
from os import listdir
from pathlib import Path
import telegram
import time
from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_some_launch
from fetch_nasa import fetch_nasa_epic_images, fetch_nasa_image_of_the_day


def download_images(path_for_images, number_of_spacex_launch, nasa_api_key):
    fetch_nasa_epic_images(path_for_images, nasa_api_key)
    fetch_spacex_some_launch(path_for_images, number_of_spacex_launch)
    fetch_nasa_image_of_the_day(path_for_images)


def send_photo_to_telegram_channel(bot, path_for_images,channel_chat_id):
    while True:
        for path_for_photo in listdir(path_for_images):
            with open(f'{path_for_images}/{path_for_photo}', 'rb') as space_photo:
                bot.send_photo(
                    chat_id=channel_chat_id,
                    photo=space_photo
                )
            time.sleep(24*60*60)


def main():
    load_dotenv()
    path_for_images = 'images'
    Path(path_for_images).mkdir(parents=True, exist_ok=True)
    number_of_spacex_launch = 60
    nasa_api_key = os.getenv('NASA_API_KEY')
    download_images(path_for_images, number_of_spacex_launch, nasa_api_key)

    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(telegram_bot_token)
    channel_chat_id = os.getenv('TELEGRAM_CHANNEL_ID')
    send_photo_to_telegram_channel(bot, path_for_images,channel_chat_id)
    

if __name__ == '__main__':
    main()


