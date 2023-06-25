import urllib.request, json
import os

file = open("./videos-para-download.json", "rb")
videos = json.load(file)
file.close()

videos_downloaded = os.listdir("./videos")

for video in videos:
    video_name = video.split("/")[-1]    
    if video_name not in videos_downloaded:
        print("Baixando ... ", video_name)
        urllib.request.urlretrieve(video, "videos/" + video_name)
    else:
        print("VIDEO JÁ PRESENTE:", video_name)