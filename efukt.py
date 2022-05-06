from f import *

def return_source_link(url):
    # url = "https://efukt.com/22269_Donnies_Feed_and_Seed.html"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    video = soup.find("source",type="video/mp4")

    return video["src"]

# convert data of csv file to dictionary with first column as value and second column of csv as key
def convert_csv_to_dict(csv_file):
    with open(csv_file, "r") as f:
        data = f.read()
        data = data.split("\n")
        data = data[1:]
        data = [x.split(",") for x in data]
        link = [x[0] for x in data]
        title = [x[1] for x in data]
        data = dict(zip(title, link))
        return data

def main():
    for title, link in convert_csv_to_dict("efukt.csv").items():
        download_video_series(f"{title}.mp4",return_source_link(link))


if __name__ == "__main__":
    main()
    
# links = ["https://cdnv.efukt.com/key=9Slxyuok9fHAOxBpmxQpIQ,end=1651744528/2017/12/df_1513370702_efuktcom.mp4"]
# import requests
# def download_video_series(video_links): 

#     for link in video_links: 

#         '''iterate through all links in video_links 
#         and download them one by one'''

#         # obtain filename by splitting url and getting  
#         # last string 
#         file_name = link.split('/')[-1]    

#         print(f"Downloading file:{file_name}") 

#         # create response object 
#         r = requests.get(link, stream = True) 

#         # download started 
#         with open(file_name, 'wb') as f: 
#             for chunk in r.iter_content(chunk_size = 1024*1024): 
#                 if chunk: 
#                     f.write(chunk) 

#         print(f"Downloaded file:{file_name}")

#     print("Download complete")
# download_video_series(links)