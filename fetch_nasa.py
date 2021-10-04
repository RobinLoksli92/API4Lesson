import requests
from fetch_spacex import split_the_expansion
from fetch_spacex import save_image_from_url
import datetime


path_for_images = 'C:/VScode_projects/API4Lesson/images'  # Укажите свой путь до папки с картинками

def fetch_nasa_image_of_the_day():
    url = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': 30,
        'api_key':'PrwXPBykBiowDIBWnlELW7tH7ooxpl343nCUhe5z',
    }

    response = requests.get(url, params=payload)
    response.raise_for_status

    pictures_of_the_day = response.json()

    for number_of_pictire, picture in enumerate(pictures_of_the_day):
        url_of_apod = picture.get('url')
        expansion_of_file = split_the_expansion(url_of_apod)
        filename = path_for_images + '/' + f'APOD_{number_of_pictire}.{expansion_of_file}'
        save_image_from_url(url_of_apod,filename)


def fetch_nasa_epic_images():
    url_for_epic = 'https://api.nasa.gov/EPIC/api/natural/images'

    payload = {
        'api_key': 'PrwXPBykBiowDIBWnlELW7tH7ooxpl343nCUhe5z',
    }

    response = requests.get(url_for_epic, params=payload)
    response.raise_for_status

    epic_pictures = response.json()

    for picture in epic_pictures[:5]:
        data = picture.get('date')
        image_name = picture.get('image')
        data = data[:10]
        data = datetime.date.fromisoformat(data)
        data = data.strftime('%Y/%m/%d')
        template_of_url = f'https://api.nasa.gov/EPIC/archive/natural/{data}/png/{image_name}.png'

        response = requests.get(template_of_url, params=payload)
        response.raise_for_status

        filename = path_for_images + '/' + f'{image_name}.png'
        with open(filename, 'wb') as file:
            file.write(response.content)

