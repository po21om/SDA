from timeit import default_timer
from matplotlib import pyplot as plt
from collections import deque

start = default_timer()
list_of_nums = []
deque_list = deque(list_of_nums)
list_of_times = []

for x in range(10_000_000):
    deque_list.append(x)
    if x % 10_000 == 0:
        list_of_times.append(default_timer() - start)

for x in range(10_000_000):
    deque_list.pop()
    if x % 10_000 == 0:
        list_of_times.append(default_timer() - start)

for x in range(10_000_000):
    deque_list.appendleft(x)
    if x % 10_000 == 0:
        list_of_times.append(default_timer() - start)

for x in range(10_000_000):
    deque_list.popleft()
    if x % 10_000 == 0:
        list_of_times.append(default_timer() - start)

plt.plot(list_of_times)
plt.show()

