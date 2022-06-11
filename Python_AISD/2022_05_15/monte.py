import random


def pi_sq(l) -> float:
    inside = 0
    for i in range(l):
        x_rand = random.random()
        y_rand = random.random()
        if 0.5**2 > (x_rand-0.5)**2 + (y_rand-0.5)**2:
            inside += 1

    return (inside/l)*4


print(pi_sq(100_000_000))