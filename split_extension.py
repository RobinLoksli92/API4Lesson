from urllib.parse import urlparse, urlsplit
import os


def split_the_extension(url):
    parsed_url = urlsplit(url)
    path_of_url = parsed_url.path
    splited_file = os.path.splitext(path_of_url)
    extension_of_file = splited_file[1]
    return extension_of_file