import os
from os import listdir
from pathlib import Path
import telegram
import time
from dotenv import load_dotenv

from fetch_spacex import fetch_spacex_last_launch
from fetch_nasa import fetch_nasa_epic_images, fetch_nasa_image_of_the_day


def main():
    url_for_hubble = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    
    Path('C:/VScode_projects/API4Lesson/images').mkdir(parents=True, exist_ok=True)

    fetch_nasa_epic_images()
    fetch_spacex_last_launch()
    fetch_nasa_image_of_the_day()

    load_dotenv()
    telegram_bot_token = os.getenv('TELEGRAM_BOT')
    bot = telegram.Bot(telegram_bot_token)
    path_for_photos = 'images'
    chat_id = '@space_photos_python_tg'  # Здесь введите телеграмм канал, в котором вы сделали администратором своего бота

    while True:
        for path_for_photo in listdir(path_for_photos):
            bot.send_photo(
                chat_id=chat_id,
                photo=open(f'images/{path_for_photo}', 'rb')
            )
            time.sleep(24*60*60)


if __name__ == '__main__':
    main()


