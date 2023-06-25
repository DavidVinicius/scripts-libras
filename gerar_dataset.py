import json
import utils
import csv
from unidecode import unidecode

def create_object(marcador):
    duration = utils.to_timedelta(marcador['durationVerse'])

    ini = utils.to_timedelta(marcador['startTime'])
    end = utils.to_timedelta(marcador['durationVerse'])
    fi = ini + end

    return {
        "duration": marcador['duration'],
        "durationText": marcador['durationVerse'],
        "startText": marcador['startTime'],
        "timestamps": [[ini.total_seconds(), fi.total_seconds()]] * 3,
        "sentences": [unidecode(marcador['verse_nwt'].replace('"', "").replace("\t", "").replace("\r", "")), 
                      unidecode(marcador['verse_acf'].replace('"', "").replace("\t", "").replace("\r", "")),
                     unidecode(marcador['verse_nvi'].replace('"', "").replace("\t", "").replace("\r", ""))
                    ],
        "book": marcador['book'],
        "bookNumber": marcador['bookNumber'],
        "chapterNumber": marcador['chapterNumber'],
        "verseNumber": marcador['verseNumber'],
    }

def create_row(filename, obj, phase, idx, verse):
    return [
        filename, 
        unidecode(verse).replace('"', "").replace("\t", "").replace("\r", ""), 
        obj['timestamps'][0][0], 
        obj['timestamps'][1][1], 
        obj['duration'], 
        phase,
        idx
    ]
def create_row_json(filename, obj, idx, phase, verse):
    return {
        "video_id": filename,
        "caption": unidecode(verse).replace('"', "").replace("\t", "").replace("\r", ""),
        "start": obj['timestamps'][0][0],
        "end": obj['timestamps'][0][1],
        "duration": obj['duration'], 
        "phase": phase,
        "idx": idx,
        "book": obj['book'],
        "bookNumber": obj['bookNumber'],
        "chapterNumber": obj['chapterNumber'],
        "verseNumber": obj['verseNumber'],
    }


csv_dataset = open('new_dataset.csv', 'w', newline='')
csv_dataset_test = open('new_dataset_test.csv', 'w', newline='')
csv_dataset_validation = open('validation_dataset.csv', 'w', newline='')

writer_csv  = csv.writer(csv_dataset, delimiter='\t')
writer_csv_test  = csv.writer(csv_dataset_test, delimiter='\t')
writer_csv_validation  = csv.writer(csv_dataset_validation, delimiter='\t')

file = open("./marcadores_final.json", "rb")
marcadores = json.load(file)
file.close()

print(len(marcadores))
dataset = []
test = []
validation = []

d = len(marcadores[:20432])
t = len(marcadores[20432:24809])
v = len(marcadores[24809:])



columns = ["video_id","caption","start","end","duration","phase","idx"]

writer_csv.writerow(columns)
counter = 0
for marcadorDataset in marcadores[:20432]:
    filename = marcadorDataset['file'].split('/')[-1]
    filename2 = filename.split('.')[0]
    obj = create_object(marcadorDataset)    
        
    writer_csv.writerow(create_row(filename=filename2, obj=obj, phase='train', idx=counter, verse=marcadorDataset['verse_nwt']))    
    dataset.append(create_row_json(filename=filename2, obj=obj, phase='train', idx=counter, verse=marcadorDataset['verse_nwt']))
    counter += 1
    
    writer_csv.writerow(create_row(filename=filename2, obj=obj, phase='train', idx=counter, verse=marcadorDataset['verse_acf']))    
    dataset.append(create_row_json(filename=filename2, obj=obj, phase='train', idx=counter, verse=marcadorDataset['verse_acf']))
    counter += 1
    
    writer_csv.writerow(create_row(filename=filename2, obj=obj, phase='train', idx=counter, verse=marcadorDataset['verse_nvi']))    
    dataset.append(create_row_json(filename=filename2, obj=obj, phase='train', idx=counter, verse=marcadorDataset['verse_nvi']))
    counter += 1
        

counter = 0
writer_csv_test.writerow(columns)
for marcadorTest in marcadores[20432:24810]:
    filename = marcadorTest['file'].split('/')[-1]

    obj = create_object(marcadorTest)    
    
    writer_csv_test.writerow(create_row(filename=filename2, obj=obj, phase='test', idx=counter, verse=marcadorTest['verse_nwt']))    
    test.append(create_row_json(filename=filename2, obj=obj, phase='test', idx=counter, verse=marcadorTest['verse_nwt']))
    counter += 1
    
    
    writer_csv_test.writerow(create_row(filename=filename2, obj=obj, phase='test', idx=counter, verse=marcadorTest['verse_acf']))    
    test.append(create_row_json(filename=filename2, obj=obj, phase='test', idx=counter, verse=marcadorTest['verse_acf']))
    counter += 1
    
    writer_csv_test.writerow(create_row(filename=filename2, obj=obj, phase='test', idx=counter, verse=marcadorTest['verse_nvi']))    
    test.append(create_row_json(filename=filename2, obj=obj, phase='test', idx=counter, verse=marcadorTest['verse_nvi']))
    counter += 1

counter = 0
writer_csv_validation.writerow(columns)

for marcadorValidation in marcadores[24810:]:
    filename = marcadorValidation['file'].split('/')[-1]
    filename2 = filename.split('.')[0]
    obj = create_object(marcadorValidation)

    writer_csv_validation.writerow(create_row(filename=filename2, obj=obj, phase='val_1', idx=counter, verse=marcadorValidation['verse_nwt']))

    validation.append(create_row_json(filename=filename2, obj=obj, phase='val_1', idx=counter, verse=marcadorValidation['verse_nwt']))
    counter += 1
    
    writer_csv_validation.writerow(create_row(filename=filename2, obj=obj, phase='val_1', idx=counter, verse=marcadorValidation['verse_acf']))
    validation.append(create_row_json(filename=filename2, obj=obj, phase='val_1', idx=counter, verse=marcadorValidation['verse_acf']))
    counter += 1
    
    writer_csv_validation.writerow(create_row(filename=filename2, obj=obj, phase='val_1', idx=counter, verse=marcadorValidation['verse_nvi']))    
    validation.append(create_row_json(filename=filename2, obj=obj, phase='val_1', idx=counter, verse=marcadorValidation['verse_nvi']))
    counter += 1



print("val1 val2", len(marcadores[26998:]))
print("test", len(marcadores[20432:24810]))
print("dataset", d)

dataset_json = json.dumps(dataset)
file2write=open("dataset.json",'w')
file2write.write(dataset_json)
file2write.close()            


test_json = json.dumps(test)
file2write=open("test_dataset.json",'w')
file2write.write(test_json)
file2write.close()

validation_json = json.dumps(validation)
file2write=open("validation_dataset.json",'w')
file2write.write(validation_json)
file2write.close()