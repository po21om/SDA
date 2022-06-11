import random
def losowanie():
    a = int(random.randint(0, 6))
    if a == 0:
        return 'a'
    elif a == 1:
        return 'b'
    elif a == 2:
        return 'c'
    elif a == 3:
        return 'd'
    elif a >= 4:
        return 'e'

print(losowanie())