import requests
import os
from split_expansion import split_the_expansion
from save_image import save_image_from_url


def fetch_spacex_last_launch(path_for_images):
    url_for_launch_number_60 = 'https://api.spacexdata.com/v3/launches/60'
    response = requests.get(url_for_launch_number_60)
    response.raise_for_status()

    rocket_info = response.json()
    links_of_launch = rocket_info['links']
    images_of_launch = links_of_launch.get('flickr_images')

    for nubmer_of_image, url_of_image in enumerate(images_of_launch):
        expansion_of_file = split_the_expansion(url_of_image)
        filename = f'{path_for_images}/spacex{nubmer_of_image}.{expansion_of_file}'
        save_image_from_url(url_of_image,filename)


def main():
    pass


if __name__ == '__main__':
    main()