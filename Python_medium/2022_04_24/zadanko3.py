import csv

with open("title_basics.csv", encoding='UTF-8') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    # for row in reader:
    #     rows.append(row)
    rows_sorted = sorted(rows, key=lambda x: int(x[5]) if x[5].isdigit() else 0, reverse=True)
    print(rows_sorted[:100])
    # print(rows_sorted[-1:-100:-1])
