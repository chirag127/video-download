
import requests
from bs4 import BeautifulSoup


# make list of all url links with class="btp_post_card__title text-decoration-none"

# def get_video_links(url):
#     ``

def get_video_links(archive_url):
    # create response object
    r = requests.get(archive_url)
    # create beautiful-soup object
    soup = BeautifulSoup(r.content, 'html5lib')
    # find all links on web-page
    links = soup.findAll('video')
    # filter the link ending with .mp4
    video_links = []
    for link in links:
        try:
            if link.get('src').endswith('.mp4'):
                video_links.append(link.get('src'))
        except Exception:
            print(f"Error: {link}")
    return video_links


# def downloadfile(url):
#     name = url.split('/')[-1]
#     name = f"{name}.mp4"
#     r = requests.get('url')
#     print("****Connected****")
#     with open(name, 'wb') as f:
#         print("Donloading.....")
#         for chunk in r.iter_content(chunk_size=255):
#             if chunk:  # filter out keep-alive new chunks
#                 f.write(chunk)
#         print("Done")


def download_video_series(video_links):

    for link in video_links:
     # iterate through all links in video_links
        # and download them one by one
        # obtain filename by splitting url and getting last string
        file_name = link.split('/')[-1]

        print(f"Downloading file:{file_name}")

        # create response object
        r = requests.get(link, stream=True)

        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All videos downloaded!")
    return


if __name__ == "__main__":
    url = "https://deepgoretube.site/"

    print("Connecting to {url}".format(url=url))

    download_video_series(get_video_links(url))