import csv
# abrindo o arquivo para escrita
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='\t')
    spamwriter.writerow(['video_id','caption','start','end','duration','category_32','subs','phase', 'idx'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])