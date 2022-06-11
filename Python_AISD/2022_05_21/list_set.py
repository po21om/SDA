from timeit import default_timer
from matplotlib import pyplot as plt

start = default_timer()
r = 1_000_000
list_of_nums = [x for x in range(r)]
list_of_times = []
for x in range(r):
    list_of_nums[x] = x*2
    if x % 1_000 == 0:
        list_of_times.append(default_timer() - start)

plt.plot(list_of_times)
plt.show()