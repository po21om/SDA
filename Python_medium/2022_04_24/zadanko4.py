import csv

with open("title_basics.csv", encoding='UTF-8') as f:
    reader = csv.reader(f)
    rows =[]
    for row in reader:
        rows.append(row)

    rows_sorted = sorted(rows, key=lambda row: int(row[-2]) if row[-2].isdigit() else 0, reverse=True)
    print(rows_sorted[0][3], rows_sorted[0][-2])

    max_len = max(rows, key=lambda row: int(row[-2]) if row[-2].isdigit() else 0)
    print(max_len[3], max_len[-2])

    # for row in rows_sorted:
    #     if row[-2].isnumeric():
    #         print(row[3],row[-2])
    #         break
    # print(row[3],row[-2] if ow[-2].isnumeric() else "")