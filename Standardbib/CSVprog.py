import csv
reader = csv.reader(open("CSV","rb"))
for row in reader:
    for item in row:
        print item
