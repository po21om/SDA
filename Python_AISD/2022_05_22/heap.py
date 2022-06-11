from heapq import heappush, heappop, heapify, _heapify_max, _heappop_max
from timeit import default_timer
import random
from matplotlib import pyplot as plt

l1 = [random.randint(1,100000) for _ in range(100_000)]
l2 = [random.randint(1,100000) for _ in range(200_000)]
l3 = [random.randint(1,100000) for _ in range(300_000)]
l4 = [random.randint(1,100000) for _ in range(400_000)]
l5 = [random.randint(1,100000) for _ in range(500_000)]
l6 = [random.randint(1,100000) for _ in range(600_000)]
l7 = [random.randint(1,100000) for _ in range(700_000)]
l8 = [random.randint(1,100000) for _ in range(800_000)]
l9 = [random.randint(1,100000) for _ in range(900_000)]
l10 = [random.randint(1,100000) for _ in range(1_000_000)]
l = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]


list_of_times = []


def heapsort(iterable):
    h =[]
    for idx, value in enumerate(iterable):
        heappush(h, value)
    #return [heappop(h) for i in range(len(h))]


for x in l:
    start = default_timer()
    heapsort(x)
    list_of_times.append(default_timer()-start)

# print()

#plt.show()

list_of_times2 = []


def heapsort2(iterable):
    heapify(iterable)
    #return [heappop(iterable) for i in range(len(iterable))]


for x in l:
    start2 = default_timer()
    heapsort2(x)
    list_of_times2.append(default_timer() - start2)

plt.plot(list_of_times, 'r')
plt.plot(list_of_times2, 'b')
plt.show()


#
#
# start = timeit()
# for _ in range(1_000_000):
#     def heapsort_max(iterable):
#         _heapify_max(iterable)
#         return [_heappop_max(iterable) for i in range(len(iterable))]
#
# #print(heapsort_max(l))
# print(timeit()-start)