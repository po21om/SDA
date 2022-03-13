# range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(5):
#     print(i)
#
# for i in range(1, 14, 3):
#     print(i)

# for i in range(1,100,2):
#     print(f"Liczba: {i}, kwadrat: {i**2}, sześcian: {i**3}")
#

#Fizz Buzz
import time

start = time.time()
for i in range(1,1001):
    if i%15 == 0:
        print(f"{i} is FizzBuzz")
    elif i%5 == 0:
        print(f"{i} is Buzz")
    elif i%3 == 0:
        print(f"{i} is Fizz")
stop = time.time()
print(stop-start)
start = time.time()
for i in range(1,1001):
    print(i, end=" ")
    if i%3 == 0:
        print("Fizz", end="")
    if i%5 == 0:
        print("Buzz")
        continue
    print("")
stop = time.time()
print(stop-start)


start = time.time()

for i in range(10000):
    a = i**2200+int("100")**3
    b = a*222-123123
    c = b*22//a**2

stop = time.time()
print(stop-start)