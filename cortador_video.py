# Import everything needed to edit video clips
from moviepy.editor import *
import json
from datetime import timedelta

def to_td(h):
    ho, mi, se = h.split(':')
    se, mili = se.split(".")
    return timedelta(hours=int(ho), minutes=int(mi), seconds=int(se), milliseconds=int(mili))
def separetate_time(h):
    try:
        ho, mi, se = h.split(':')
        se, mili = se.split(".")
        se = int(round(float(se)))
        return (int(ho), int(mi), se)
    except:
        print("falha ao aredondar: ", h)
        ho, mi, se = h.split(':')
        se = int(round(float(se)))
        return (int(ho), int(mi), se)

file = open("./marcadores.json", "rb")
marcadores = json.load(file)
verso1 = marcadores[0]
ini = to_td(verso1['startTime'])
end = to_td(verso1['duration'])
fi = ini + end

print(fi)


# loading video gfg
clip = VideoFileClip("nwt_01_Ge_LSB_01_r720P.mp4")
# getting only first 5 seconds
clip = clip.subclip(separetate_time(verso1['startTime']), separetate_time(str(fi)))
# showing clip
clip.ipython_display(width = 360)
print(verso1['label'])
print(verso1['verse_acf'])
print(verso1['verse_nvi'])