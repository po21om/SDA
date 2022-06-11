#gen = (a + a[-1] for a in range(10))
#for x in gen:
#    print(x)


def fibo_generator(n):
    number = 0
    a = 1
    b = 1
    while number < 2:
        yield 1
        number += 1
    while number != n:
        a, b = b, a+b
        yield b
        number += 1

fibo = fibo_generator(10)

for elem in fibo:
    print(elem)