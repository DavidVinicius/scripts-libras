# -*- coding: utf-8 -*-
import json, os, csv

#json.loads("./")
arquivos = os.listdir("./marcadores")
counter = 0
dataRows = []
dataJson = []

file = open("./bible_acf.json", "rb")
bible_acf = json.load(file)
file.close()

file = open("./bible_aa.json", "rb")
bible_aa = json.load(file)
file.close()

file = open("./bible_nvi.json", "rb")
bible_nvi = json.load(file)
file.close()
file = open("./biblia_nwt.json", "rb")
bible_nwt = json.load(file)
file.close()

#print(len(bible_nwt[45]['capitulos']), len(bible_nvi[45]['chapters']))
#print(bible_nwt[45]['nome'], (bible_nvi[45]['name']))

#exit()

for arquivo in arquivos:
    file = open("./marcadores/" + arquivo)
    t = json.load(file)
    print(">>", arquivo)
    for chapter in t["files"]["LSB"].get("MP4", "M4V"):
        if "markers" in chapter and chapter["markers"] != None:
            print(t['pubName'], chapter['title'])
            book = chapter["markers"]['bibleBookNumber']
            chapterNumber = chapter["markers"]['bibleBookChapter']
            chapter["markers"]['BookName'] = t['pubName']
            chapter["markers"]['file'] = chapter['file']['url']
            for verse in chapter['markers']['markers']:
                print(book, bible_nvi[book-1].get("abbrev"), bible_nwt[book-1].get("Livro"), chapterNumber, verse['verseNumber'])
                text_acf = bible_acf[book-1]['chapters'][chapterNumber-1][verse['verseNumber']-1]
                text_aa =""# bible_aa[book-1]['chapters'][chapterNumber-1][verse['verseNumber']-1]
                text_nvi = bible_nvi[book-1]['chapters'][chapterNumber-1][verse['verseNumber']-1]
                text_nwt = bible_nwt[book-1]['capitulos'][chapterNumber-1][verse['verseNumber']-1]
                #print(text)
                # dataRows.append([
                #     t['pubName'], book, chapterNumber, verse['verseNumber'], verse['label'], verse['startTime'], verse['duration'], verse['endTransitionDuration'], chapter['file']['url'], text
                # ])

                dataJson.append({
                    "book": t['pubName'],
                    "bookNumber": book,
                    "chapterNumber": chapterNumber,
                    "verseNumber": verse['verseNumber'],
                    "label": verse['label'],
                    "startTime": verse['startTime'],
                    "durationVerse": verse['duration'],
                    "duration": chapter['duration'],
                    "endTransitionDuration": verse['endTransitionDuration'],
                    "file": chapter['file']['url'],
                    "verse_acf": text_acf,
                    "verse_aa": text_aa,
                    "verse_nvi": text_nvi,
                    "verse_nwt": text_nwt,
                })
                            

    
    counter += 1
    file.close()    
    #if counter == 3:
    #    break
header = ["book", "bookNumber", "chapterNumber", "verseNumber", "label", "startTime", "duration", "endTransitionDuration", "file", "verseText"]
#print(dataRows)
data = json.dumps(dataJson)
file2write=open("marcadores_final.json",'w')
file2write.write(data)
file2write.close()            
'''

with open('./marcadores.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(dataRows)
'''