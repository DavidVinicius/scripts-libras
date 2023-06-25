import json

file = open("./bible_acf.json", "rb")
bible = json.load(file)
print(bible[1]['chapters'][1][0])