def mat_mul(A, B):
    a, b, c, d = A
    e, f, g, h = B

    return a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h


def fibo(n):
    x = (1, 1, 1, 0)
    z = (1, 1, 1, 0)
    while n > 0:
        if n % 2:
            z = mat_mul(x, z)
        x = mat_mul(x, x)
        n //= 2
    a, b, c, d = z
    return d


for i in range(1_000):
    print(fibo(i))

print(fibo(1_000_000))
