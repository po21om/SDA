import csv
import timeit
import requests

tconsts = []

with open("cut_films.csv", encoding='UTF-8', ) as f:
    reader = csv.reader(f)
    for row in reader:
        tconsts.append(row[0])


tconsts = tconsts[1:]
https = ['https://www.imdb.com/title/'+x+'/' for x in tconsts]
#print(https)

def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, "a") as f:
            f.write(result)

    except requests.exceptions.RequestException:
        print("Error with URL check!")

def with_threading_func(urls):
    import threading

    threads = []
    for url, tconst in zip(urls, tconsts):
        th = threading.Thread(target=crawl, args=(url, f'data/{tconst}.html'))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


with_threading_func(https)



