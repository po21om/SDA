from math import sqrt, inf
import numpy as np
import copy
# AB = pier (xb - xa)2 + (yb - ya)2

def xy_space(la, lb):
    xa, ya = la
    xb, yb = lb
    result = sqrt((xb - xa)**2 + (yb - ya)**2)
    return result

cities = [[0,0],[5,4],[10,7],[3,8],[6,9],[1,2],[4,5]]

N = 100
xx = np.random.randint(0,1000,N)
yy = np.random.randint(0,1000,N)
cities_random = [[x,y] for [x,y] in zip(xx,yy)]


def komi(l):
    route = []
    for x in range(len(l)):
        l_copy = copy.deepcopy(l)
        start_pos = l_copy[x]
        route = [l_copy[x]]
        for _ in range(len(l_copy)-1):
            space = inf
            min_i = 0
            temp_pos = 0
            for i, pos in enumerate(l_copy[1:]):
                if xy_space(start_pos, pos) < space:
                    space = xy_space(start_pos, pos)
                    temp_pos = pos
                    min_i = i + 1
            l_copy[min_i] = [inf, inf]
            route.append(temp_pos)
            start_pos = temp_pos
    return route


path = komi(cities_random)
print(cities_random)
print(path)
from matplotlib import pyplot as plt
xs = [x for [x,y] in path]
ys = [y for [x,y] in path]
plt.plot(xs, ys)
plt.show()