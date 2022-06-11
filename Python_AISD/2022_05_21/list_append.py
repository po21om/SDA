from timeit import default_timer
from matplotlib import pyplot as plt

start = default_timer()
list_of_nums = []
list_of_times = []
for x in range(10_000_000):
    list_of_nums.append(x)
    if x % 10_000 == 0:
        list_of_times.append(default_timer() - start)

plt.plot(list_of_times)
plt.show()