import csv
import threading

import requests


data = []
with open('cut_films.csv', 'r') as file:
    reader = csv.reader(file)
    batch = []

    # data = [row for row in reader]
    for row in reader:
        if row[0] == 'tconst':
            continue
        if len(batch) == 30:
            data.append(batch)
            batch = [row[0]]
        else:
            batch.append(row[0])
    if len(batch) != 0:
        data.append(batch)

# def crawl(url, dest):
#     result = requests.get(url).text
#     with open(dest, "a") as f:
#         f.write(result)

def download_batch(titles):
    for title in titles:
        result = requests.get(f'https://www.imdb.com/title/{title}').text
        with open(f'data/{title}.html', 'w', encoding="UTF-8") as f:
            f.write(result)



threads = []
for batch in data:
    th = threading.Thread(target=download_batch, args=(batch,))
    th.start()
    threads.append(th)

for th in threads:
    th.join()

# def crawl(url, dest):
#     result = requests.get(url).text
#     with open(dest, "a") as f:
#         f.write(result)
#
#
# for row in data:
#     if row[0] == 'tconst':
#         continue
#     crawl(f'https://www.imdb.com/title/{row[0]}', f'data/{row[0]}.html')
