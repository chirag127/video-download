import requests
from bs4 import BeautifulSoup



def get_video_links(url):
    #create response object
    r = requests.get(url)
    #create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')
    #find all links on web-page
    links = soup.findAll('source')
    return [link['src'] for link in links if link.has_attr('src')]

def download_video_series(video_links):
    for link in video_links:
        filename = link.split('/')[-1]
        r = requests.get(link)
        with open(f'/Videos/{filename}', 'wb') as f:
            f.write(r.content)

def download_video(link):
    filename = link.split("/")[-1]
    r = requests.get(link)
    with open(f"b/{filename}", "wb") as f:
        f.write(r.content)



if __name__ == "__main__":



    page = requests.get("https://crazyshit.com/videos/",timeout=5)

    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all("a", class_="thumb")

    links = [link["href"] for link in links]

    urls = links
    for url in urls:
        print(f"Downloading series from {url}")
        video_links = get_video_links(url)
        print(f"Found {len(video_links)} videos")

        for link in video_links:
            print(link)
            # replace speed=1.3 with speed=6.0 to download faster
            download_video(link)
