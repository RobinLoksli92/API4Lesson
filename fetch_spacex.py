import requests
import os
from urllib.parse import urlparse, urlsplit


path_for_images = 'C:/VScode_projects/API4Lesson/images'


def split_the_expansion(url):
    parsed_url = urlsplit(url)
    path_of_url = parsed_url.path
    splited_file = os.path.splitext(path_of_url)
    expansion_of_file = splited_file[1]
    return expansion_of_file


def save_image_from_url(url, filename):
    response = requests.get(url)
    response.raise_for_status

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url_for_launch_number_60 = 'https://api.spacexdata.com/v3/launches/60'
    
    response = requests.get(url_for_launch_number_60)
    response.raise_for_status

    rocket_info = response.json()
    links_of_launch = rocket_info['links']
    images_of_launch = links_of_launch.get('flickr_images')

    for nubmer_of_image, url_of_image in enumerate(images_of_launch):
        response = requests.get(url_of_image)
        response.raise_for_status
        expansion_of_file = split_the_expansion(url_of_image)

        filename = path_for_images + '/' + f'spacex{nubmer_of_image}.{expansion_of_file}'

        save_image_from_url(url_of_image,filename)
