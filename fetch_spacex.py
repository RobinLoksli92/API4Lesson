import requests
from split_extension import split_extension
from save_image import save_image_from_url


def fetch_spacex_some_launch(images_path,spacex_launch_number):
    some_launch_launch = f'https://api.spacexdata.com/v3/launches/{spacex_launch_number}'
    response = requests.get(some_launch_launch)
    response.raise_for_status()

    rocket_info = response.json()
    launch_links = rocket_info['links']
    launch_images = launch_links.get('flickr_images')

    for image_number, image_url in enumerate(launch_images):
        file_extension = split_extension(image_url)
        filename = f'{images_path}/spacex{image_number}.{file_extension}'
        save_image_from_url(image_url, filename)
