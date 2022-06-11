my_lambda = lambda x: x.lower()
print(my_lambda("HA HA HA"))

square_lambda = lambda x: x ** 2
print(square_lambda(16))

equals_lambda = lambda x, y: x == y
print((equals_lambda(3, 4)))

items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, items))
print(squared)

odds = list(filter(lambda x: x % 2, items))
print(odds)

from functools import reduce
items_sum = reduce(lambda x, y: x + y, items)
print(items_sum)

pairs = [(1, 10), (2, 9), (3, 8)]
print(pairs)
print(sorted(pairs, key=lambda x: x[1]))

print(min(pairs))
print(max(pairs, key=lambda x: x[1]))
print(max(pairs, key=lambda x: x[0] * x[1]))