import time
import numpy as np


def select_sort(list) -> list:
    for i in range(len(list)):
        min_i = i
        for j in range(i+1,(len(list))):
            if list[min_i] > list[j]:
                min_i = j
        list[i], list[min_i] = list[min_i], list[i]
    return list


a = list(np.random.rand(100_000))
start = time.time()
select_sort(a)
end = time.time()
print(end-start)


# czasowa O(n**2) 2 petle po n wiec n*n
# pamięciowa O(1) stała ilość pamieci bez różnicy na wielkość listy (i, j, min_i, zmienna przy swapie)