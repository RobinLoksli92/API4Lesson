import requests
from split_expansion import split_the_extension
from save_image import save_image_from_url


def fetch_spacex_some_launch(path_for_images,number_of_launch):
    url_for_some_launch = f'https://api.spacexdata.com/v3/launches/{number_of_launch}'
    response = requests.get(url_for_some_launch)
    response.raise_for_status()

    rocket_info = response.json()
    links_of_launch = rocket_info['links']
    images_of_launch = links_of_launch.get('flickr_images')

    for nubmer_of_image, url_of_image in enumerate(images_of_launch):
        expansion_of_file = split_the_extension(url_of_image)
        filename = f'{path_for_images}/spacex{nubmer_of_image}.{expansion_of_file}'
        save_image_from_url(url_of_image,filename)


def main():
    pass


if __name__ == '__main__':
    main()