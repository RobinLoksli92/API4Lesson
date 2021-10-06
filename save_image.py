import requests


def save_image_from_url(url, filename, params=None):
    response = requests.get(url,params)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)