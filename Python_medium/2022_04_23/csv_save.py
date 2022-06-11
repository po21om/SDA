import csv

with open('pracownicy.csv', 'a', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Johnny Bravo', 6900])
    #writer.writerows([['Johnny Bravo', 6900],['Anna H', 5600]])