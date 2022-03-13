owoce = ["Arbuz", "Ananas", "Banan", "Kiwi", "Mandarynka", "Jabłko"]

for owoc in owoce:
    if len(owoc) == 10:
        print(f"10-literowy owoc: {owoc}")
        break
    if owoc == "Banan":
        print(f"{owoc.upper()}")
        continue
    if owoc == "Kiwi":
        print(f"{owoc} to mój ulubiony owoc.")
        continue
    print(owoc)