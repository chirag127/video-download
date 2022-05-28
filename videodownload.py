import requests

with open("already_downloaded.txt", "r") as f:
    already_downloaded = f.readlines()
    already_downloaded = [x.strip() for x in already_downloaded]
    print(already_downloaded)



def download_video_series():

    # get all url from a file csv
    with open('deepgoretube.csv', 'r') as f:
        lines = f.readlines()

        # remove header
        lines = lines[1:]

        

        for line in lines:
            line = line.strip()
            line = line.split(',')
            url = line[0]
            badge = line[1]
            badge = badge.replace("p", '')
            new_url_ext = f"Up-{badge}.mp4"
            url = url.replace('Photo-0001.jpg', new_url_ext)
            
            if url not in already_downloaded:
                print(url)
                download_video(url)



def download_video(link):
    '''iterate through all links in video_links 
    and download them one by one'''

    # obtain filename by splitting url and getting
    # last string
    file_name = link.split('/')[-1]

    print(f"Downloading file:{file_name}")

    # create response object
    
    r = requests.get(link, stream=True)
    # download started
    # file_name = file_name.replace('-Up-', '')
    # file_name = file_name.replace('.mp4', '')
    # file_name = file_name.replace('-', '_')
    file_name = f"deepgore/{file_name}"

    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

        print("%s downloaded!\n" % file_name)
        with open("already_downloaded.txt", "a") as f:
            f.write(link + "\n") 


    else:
        print(f"Failed to download {file_name}")
        print(r.status_code)

if __name__ == '__main__':
    download_video_series()
