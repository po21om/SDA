import csv

with open("title_basics.csv", 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
#    for row in reader:
#        rows.append(row)
#    for row in rows[:100]:
#        print(row)

#    rows =[row for row in reader]
#    print(rows[:100])

    for idx, row in enumerate(reader):
        print(row)
        if idx == 100:
            break