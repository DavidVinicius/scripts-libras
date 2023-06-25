import json
from moviepy.editor import *
from datetime import timedelta
import os

file = open("./marcadores.json", "rb")
marcadores = json.load(file)
file.close()

def to_td(h):
    ho, mi, se = h.split(':')
    se, mili = se.split(".")
    return timedelta(hours=int(ho), minutes=int(mi), seconds=int(se), milliseconds=int(mili))
def separetate_time(h):
    ho, mi, se = h.split(':')
    se, mili = se.split(".")
    se = int(round(float(se)))
    return (int(ho), int(mi), se)

for marcador in marcadores:
    file = marcador['file'].split('/')[-1]
    print(file)    
    versiculo_name = f"./versiculos/{marcador['bookNumber']}_{marcador['chapterNumber']}_{marcador['verseNumber']}_" + file

    if not os.path.exists(versiculo_name):
        ini = to_td(marcador['startTime'])
        end = to_td(marcador['duration'])
        fi = ini + end

        clip = VideoFileClip("videos/" + file)
        clip = clip.subclip(separetate_time(marcador['startTime']), separetate_time(str(fi)))
        clip.write_videofile()
    else:
        print("EXISTE", versiculo_name)
    break