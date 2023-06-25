import json
file = open("./marcadores.json", "rb")
marcadores = json.load(file)
file.close()

videos = []

for marcador in marcadores:
    if marcador['file'] not in videos:
        videos.append(marcador['file'])
print(videos)

data = json.dumps(videos)
file2write=open("videos-para-download.json",'w')
file2write.write(data)
file2write.close()            
