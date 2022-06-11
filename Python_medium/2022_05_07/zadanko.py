# Napisz program, który posortuje liczby, używając algorytmu SleepSort.
# UWAGA: Ten algorytm to ciekawostka, nie jest on ani rzetelnym ani wydajnym rozwiązaniem!
# Polega on na wykorzystaniu funkcji sleep(). A dokładnie:
# Dla każdej z tych liczb tworzymy osobny wątek i usypiamy go funkcją sleep na czas proporcjonalny do wartości danej liczby. Wiadomo, że najszybciej skończy się wykonywać wątek, który został uśpiony na najmniejszą ilość czasu a więc ten, który miał najmniejszą liczbę. Po funkcji sleep można dodawać te liczby do kolekcji w ten sposób otrzymując efekt sortowania.
import time
import threading

to_be_sorted = [6, 23, 8, 34, 0, 24, 2]
list_to_sort = [1, 3,  13, 16, 6, 18, 0, 2, 5, 4]
sleep_sorted = []
sleep_sorted2 = []


def sleeping(num, sorted_list, base_num, reverse=False):
    if reverse:
        time.sleep((base_num-num) * 0.1)
    else:
        time.sleep(num * 0.01)
    sorted_list.append(num)


def sleepsort(list, list2, reverse):
    threads = []
    base_num = max(list)
    for num in list:
        t = threading.Thread(target=sleeping, args=(num, list2, base_num, reverse))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


sleepsort(to_be_sorted, sleep_sorted, reverse=False)

print(sleep_sorted)

sleepsort(list_to_sort, sleep_sorted2, reverse=True)

print(sleep_sorted2)
