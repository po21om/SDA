import random

a = [random.randint(1, 100000) for _ in range(1000)]

for idx, num in enumerate(a):
    print(f'{idx}: {num}')