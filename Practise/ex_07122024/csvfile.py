import csv

with open("testdata.csv") as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        print(col[0],sep="|")
