for i in range(1,11):
    print(i)

print([i for i in range(1,11)])

a = []
for i in range(1,11):
    a.append(i)
print(a)

b = [(i, i**2) for i in range(10)]
print(b)


c = [[i, (i**2, i**3)] for i in range(10)]
print(c)

owoce = ["anANas", "baNan", "jabłko"]
poprawione_owoce = [owoc.capitalize() for owoc in owoce]
print(poprawione_owoce)