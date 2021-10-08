import requests
import os
from split_expansion import split_the_extension
from save_image import save_image_from_url
import datetime
from dotenv import load_dotenv, main
from pprint import pprint


def fetch_nasa_image_of_the_day(path_for_images):
    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': 30,
        'api_key':'PrwXPBykBiowDIBWnlELW7tH7ooxpl343nCUhe5z',
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures_of_the_day = response.json()

    for number_of_pictire, picture in enumerate(pictures_of_the_day):
        url_of_apod = picture.get('url')
        pprint(url_of_apod)
        expansion_of_file = split_the_extension(url_of_apod)
        filename = f'{path_for_images}/APOD_{number_of_pictire}.{expansion_of_file}'
        save_image_from_url(url_of_apod,filename)


def fetch_nasa_epic_images(path_for_images):
    load_dotenv()
    url_for_epic = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        'api_key': os.getenv('NASA_API_KEY')
    }

    response = requests.get(url_for_epic, params=payload)
    response.raise_for_status()

    epic_pictures = response.json()

    for picture in epic_pictures[:5]:
        data = picture.get('date')
        image_name = picture.get('image')
        data = data[:10]
        data = datetime.date.fromisoformat(data)
        data = data.strftime('%Y/%m/%d')
        template_of_url = f'https://api.nasa.gov/EPIC/archive/natural/{data}/png/{image_name}.png'
        filename = f'{path_for_images}/{image_name}.png'
        save_image_from_url(template_of_url, filename, params=payload)
        with open(filename, 'wb') as file:
            file.write(response.content)


def main():
    pass
    

if __name__ == '__main__':
    main()