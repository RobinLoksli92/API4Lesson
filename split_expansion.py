from urllib.parse import urlparse, urlsplit
import os


def split_the_expansion(url):
    parsed_url = urlsplit(url)
    path_of_url = parsed_url.path
    splited_file = os.path.splitext(path_of_url)
    expansion_of_file = splited_file[1]
    return expansion_of_file