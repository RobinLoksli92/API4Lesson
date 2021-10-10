import os
from urllib.parse import urlparse, urlsplit


def split_extension(url):
    parsed_url = urlsplit(url)
    url_path = parsed_url.path
    splited_file = os.path.splitext(url_path)
    file_extension = splited_file[1]
    return file_extension