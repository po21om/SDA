#Lista, w której szukamy element x za pomocą binarnego wyszukiwania
import time

def binary_search(L,x):
    a = 0
    b = len(L) - 1
    while (b-a) > 1:
        c = int((a + b) / 2)
        if L[c]==x:
            return True
        else:
            if L[c] > x:
                b = c
            else:
                a = c
    if L[a]== x or L[b] == x:
        return True
    else:
        return False

start = time.time()
print(binary_search(range(1_000_000_000),9))

end = time.time()
print(end-start)