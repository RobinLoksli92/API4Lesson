import requests
from split_expansion import split_the_extension
from save_image import save_image_from_url


def fetch_spacex_some_launch(images_path,spacex_launch_number):
    url_for_some_launch = f'https://api.spacexdata.com/v3/launches/{spacex_launch_number}'
    response = requests.get(url_for_some_launch)
    response.raise_for_status()

    rocket_info = response.json()
    launch_links = rocket_info['links']
    launch_images = launch_links.get('flickr_images')

    for image_number, image_url in enumerate(launch_images):
        expansion_of_file = split_the_extension(image_url)
        filename = f'{images_path}/spacex{image_number}.{expansion_of_file}'
        save_image_from_url(image_url, filename)
