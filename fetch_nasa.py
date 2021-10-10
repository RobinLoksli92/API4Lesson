import datetime
import requests

from save_image import save_image_from_url
from split_extension import split_extension


def fetch_nasa_image_of_the_day(images_path,nasa_api_key):
    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': 30,
        'api_key':nasa_api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures_of_the_day = response.json()

    for pictire_number, picture in enumerate(pictures_of_the_day):
        apod_url = picture.get('url')
        file_extension = split_extension(apod_url)
        filename = f'{images_path}/APOD_{pictire_number}.{file_extension}'
        save_image_from_url(apod_url,filename)


def fetch_nasa_epic_images(images_path, nasa_api_key):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key':nasa_api_key
    }

    response = requests.get(epic_url, params=payload)
    response.raise_for_status()

    epic_pictures = response.json()

    for picture in epic_pictures[:5]:
        date = picture.get('date')
        image_name = picture.get('image')
        date = date[:10]
        date = datetime.date.fromisoformat(date)
        date = date.strftime('%Y/%m/%d')
        url_template = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png'
        filename = f'{images_path}/{image_name}.png'
        save_image_from_url(url_template, filename, params=payload)