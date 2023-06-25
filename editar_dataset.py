import csv


file_name = "/home/valter/Downloads/arquivos_datasets/datasets/train_meta_libras.csv"
new_file = "/home/valter/Downloads/arquivos_datasets/datasets/new_train_meta_libras.csv"
phase = "train"

#file_name = "/home/valter/Downloads/arquivos_datasets/datasets/val1_meta_libras.csv"
#new_file = "/home/valter/Downloads/arquivos_datasets/datasets/new_val1_meta_libras.csv"
#phase = "val_1"

#file_name = "/home/valter/Downloads/arquivos_datasets/datasets/val1_meta_libras.csv"
#new_file = "/home/valter/Downloads/arquivos_datasets/datasets/new_val2_meta_libras.csv"
#phase = "val_2"


new_data = []
idx = 0

d = ["video_id","caption","start","end","duration","phase","idx"]
new_data.append(d)

with open(file_name,"r") as f:
    data = csv.reader(f, delimiter="\t")
    for i, linha in enumerate(data):
        if i != 0:
            d = []
            d.append(linha[0])
            d.append(linha[1])
            d.append(linha[2])
            d.append(linha[3])
            d.append(linha[4])
            d.append(phase)
            d.append(idx)
            idx = idx + 1
            new_data.append(d)

with open(new_file,"w") as f:    
    for line in new_data:
        for d in line[:-1]:
            f.write(d+"\t")
        f.write(str(line[-1])+"\n")