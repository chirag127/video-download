# print the html of https://crazyshit.com/videos/

import requests
from bs4 import BeautifulSoup

url = 'https://deepgoretube.site/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())