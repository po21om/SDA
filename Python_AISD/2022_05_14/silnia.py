def silnia(n):
    if n > 0:
        return n * silnia(n-1)
    return 1


# print(silnia(5.5))


def silna_fact(n, memory={0: 1, 1: 1}):
    if n in memory:
        return memory[n]
    memory[n] = n * silna_fact(n-1)
    return memory[n]


def fact(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


print(fact(1_000_000))


def fibo1(n, m, x):
    n, m = m, n + m
    if m < x:
        return fibo1(n, m, x)
    return m


# print(fibo1(1, 2, 100))


def fibon(n, mem={0: 0, 1: 1}):
    if n in mem:
        return mem[n]
    mem[n] = fibon(n-1) + fibon(n-2)
    return mem[n]


# print(fibon(10))


def fibo_func(n):
    x, y = 0, 1
    for _ in range(1, n+1):
        x, y = y, y + x
    return x


# print(fibo_func(10))

import sys
from functools import cache
sys.setrecursionlimit(2002)


@cache
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)


print(fibo(1000))
