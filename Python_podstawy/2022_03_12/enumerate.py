chlopcy = ["Janek", "Tomek", "Romek"]
dziewczynki = ["Ania", "Basia", "Zosia"]

for i, d in enumerate(dziewczynki):
    print(f"{d} - {chlopcy[i]}")

for item in enumerate(dziewczynki):
    print(f"{item[1]} - {chlopcy[item[0]]}")