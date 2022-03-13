# LIsta liczb od 1 do 1000 podzielnych przez 17
# wyppisac ze suma cyfr liczby x > 12

a = [num for num in range(17, 1001, 17)]
for num in a:
    c_sum = 0
    for c in str(num):
        c_sum += int(c)
    if c_sum > 12:
        print(f"Suma cyfr {c_sum} liczby {num} jest większa od 12.")

for num in a:
    if sum([int(y) for y in str(num)]) > 12:
        print(f"Suma cyfr {sum([int(y) for y in str(num)])} liczby {num} jest większa od 12.")