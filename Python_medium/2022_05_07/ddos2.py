import timeit
import requests

def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, "a") as f:
            f.write(result)

    except requests.exceptions.RequestException:
        print("Error with URL check!")



def with_threading_func(urls):
    import multiprocessing

    threads = []
    for url in urls:
        th = multiprocessing.Process(target=crawl, args=(url, "with_threads.txt"))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()


if __name__ == "__main__":
        with_proc = "with_threading_func(urls)"

        setup = '''
from __main__ import with_threading_func

urls = [
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me",
    "https://986c-83-8-50-245.ngrok.io/attack_me"
]
        '''

        print("Z watkami", timeit.timeit(stmt=with_proc,
                                         setup=setup,
                                         number=1000000))