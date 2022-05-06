
from bs4 import BeautifulSoup
import cloudscraper


def return_source_link(url):

    url = "https://theync.com/mans-face-ripped-out-in-horrible-accident.htm"

# Adding Browser / User-Agent Filtering should help ie. 

# will give you only desktop firefox User-Agents on Windows
    scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})

    html = scraper.get(url).content

    soup = BeautifulSoup(html, 'html.parser')

    print(soup) 


    video = soup.find("video",class_="jw-video")

    return video["src"]

return_source_link("https://theync.com/mans-face-ripped-out-in-horrible-accident.htm")