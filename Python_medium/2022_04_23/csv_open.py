import csv

with open("pracownicy.csv", encoding='UTF-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)