import urllib.request, json 
books = { "1":"Gênesis", "2":"Êxodo", "3":"Levítico", "4":"Números", "5":"Deuteronômio", "6":"Josué", "7":"Juízes", "8":"Rute", "9":"1 Samuel", "10":"2 Samuel", "11":"1 Reis", "12":"2 Reis", "13":"1 Crônicas", "14":"2 Crônicas", "15":"Esdras", "16":"Neemias", "17":"Ester", "18":"Jó", "19":"Salmos", "20":"Provérbios", "21":"Eclesiastes", "22":"Cântico de Salomão", "23":"Isaías", "24":"Jeremias", "25":"Lamentações", "26":"Ezequiel", "27":"Daniel", "28":"Oseias", "29":"Joel", "30":"Amós", "31":"Obadias", "32":"Jonas", "33":"Miqueias", "34":"Naum", "35":"Habacuque", "36":"Sofonias", "37":"Ageu", "38":"Zacarias", "39":"Malaquias", "40":"Mateus", "41":"Marcos", "42":"Lucas", "43":"João", "44":"Atos", "45":"Romanos", "46":"1 Coríntios", "47":"2 Coríntios", "48":"Gálatas", "49":"Efésios", "50":"Filipenses", "51":"Colossenses", "52":"1 Tessalonicenses", "53":"2 Tessalonicenses", "54":"1 Timóteo", "55":"2 Timóteo", "56":"Tito", "57":"Filêmon", "58":"Hebreus", "59":"Tiago", "60":"1 Pedro", "61":"2 Pedro", "62":"1 João", "63":"2 João", "64":"3 João", "65":"Judas", "66":"Apocalipse" }

for index, book in books.items():
    print(index, book)
    with urllib.request.urlopen(f"https://b.jw-cdn.org/apis/pub-media/GETPUBMEDIALINKS?booknum={index}&output=json&pub=nwt&alllangs=0&langwritten=LSB&txtCMSLang=LSB") as url:
        data = json.dumps(json.load(url), indent=4)        
        file2write=open(f"marcadores/{index}-{book}.json",'w')
        file2write.write(data)
        file2write.close()        