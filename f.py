import requests
from bs4 import BeautifulSoup

def download_video_series(title, link):
    import urllib.request
    urllib.request.urlretrieve(link, title)

