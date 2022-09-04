with open("all_video_links.txt", "r") as f:
    links = f.readlines()
    links = [link.strip() for link in links]


import requests


def download_video(link):
    filename = link.split("/")[-1]
    r = requests.get(link)
    with open(f"a/{filename}", "wb") as f:
        f.write(r.content)


for link in links:
    print(f"Downloading video from {link}")
    download_video(link)
