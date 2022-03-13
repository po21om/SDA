owoce = ["Arbuz", "Ananas", "Banan", "Jabłko", "Kiwi", "Kumkwat"]
# glodny = True
# while glodny:
#     print(owoce)
#     glodny = False
#
#
#n = 0
# while n < len(owoce):
#     print(owoce[n])
#     n += 1

# n = 0
# while n < len(owoce):
#     if len(owoce[n]) != 5:
#         print(owoce[n])
#         n += 1
#         continue
#     print(f"{owoce[n]} to mój ulubiony owoc")
#     n += 1
#
# n = 0
# while n < len(owoce):
#     if len(owoce[n]) < 5:
#         print(f"{owoce[n]} to mój ulubiony owoc")
#     elif len(owoce[n]) == 7:
#         break
#     elif "z" in owoce[n]:
#         print(owoce[n].upper())
#     else:        print(owoce[n])
#     n += 1
#


# list = [1,2,5,1,1,7,3,4,1]
# print(len(list)-list.count(1))



owoce = ["Arbuz", "Ananas", "Banan", "Kiwi", "Mandarynka", "Jabłko"]
n = 0
while n < len(owoce):  # n < 6
    if len(owoce[n]) == 10:
        print(f"10-literowy owoc: {owoce[n]}")
        break
    if owoce[n] == "Banan":
        print(f"{owoce[n].upper()}")
        n += 1
        continue
    if owoce[n] == "Kiwi":
        print(f"{owoce[n]} to mój ulubiony owoc.")
        n += 1
        continue
    print(owoce[n])
    n += 1  # n == 1

print("Za pętlą.")