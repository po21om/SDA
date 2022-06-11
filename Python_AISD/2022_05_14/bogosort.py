# import random
#
#
# def bogosort(l):
#     for i, x in enumerate(l):
#         if not x <= l[i+1]:
#             random.sample(l, k=len(l))
#
#



from random import shuffle

def is_sorted(data) -> bool:
    return all(a <= b for a, b in zip(data, data[1:]))

def bogosort(data) -> list:
    while not is_sorted(data):
        shuffle(data)
    return data

print(bogosort([1,5,8,0,56,3,67,23,8,89]))
