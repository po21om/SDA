import timeit

setup = "from math import sqrt"

code = '''
def func():
    l = []
    for x in range(10000000):
        l.append(x**x)
'''

print(timeit.timeit(stmt=code, number=10000000))

code2 = '''
def func():
    return [x**x for x in range(10000000)]
'''
print(timeit.timeit(stmt=code2, number=10000000))