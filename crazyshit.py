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

if __name__ == "__main__":

	with open('cs.txt', 'r') as f:
		urls = f.readlines()


	for url in urls:    
		print(f"Downloading series from {url}")
		video_links = get_video_links(url)
		print(f"Found {len(video_links)} videos")

		with open('all_video_links.txt', 'a') as f:
			for link in video_links:
				f.write(f"{link}\n")