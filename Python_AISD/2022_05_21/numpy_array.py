import numpy as np
from timeit import default_timer

start = default_timer()
l_comp = [x**2 for x in range(1_000_000)]
print('list comp.:', default_timer() - start)

l = [x for x in range(1_000_000)]

start = default_timer()
l_2 = []
for x in l:
    l_2.append(x**2)
print('for each append:', default_timer() - start)

start = default_timer()
l_map = list(map(lambda x:x**2, l))
print('map:', default_timer() - start)

l_np = np.array(l)

start = default_timer()
l_np_2 = l_np**2
print('np array:', default_timer() - start)




