import random
imie = ["Eryk", "Zygfyd", "Tobiasz", "Tifa", "Aeris", "Yufi"]
# postacie = [[(imie[random.randint(0,5)]),[random.randint(17,70), random.randint(300,450000)]] for num in range(3)]
# print(postacie)

def generator_postaci() -> dict:
    postac = {
        "imię" : imie[random.randint(0,5)],
        "wiek" : random.randint(17,70),
        "konto" : random.randint(300,450000)
    }
    return postac

# osoba = generator_postaci()
# print(osoba)

def get_job(dict):
    dict.update({"praca" : bool(random.getrandbits(1))})
    return dict
# get_job(osoba)

# print(osoba)

def married(dict):
    dict.update({"ślub" : bool(random.getrandbits(1))})
    return dict
# married(osoba)

# print(osoba)

# 50 osób w 1 zmiennej

społecznstwo = [generator_postaci() for a in range(50)]
#print(społecznstwo)
for osoba in społecznstwo:
    get_job(osoba)
    married(osoba)
#print(społecznstwo)

# 50+ bez pracy
# po ślubie przed 40
# ponizej 20 po slubie i z pracą
# wiek równo 70 lat i z literą "t" w imieniu


# print(sum[osoba["konto"] if osoba["wiek"] == 70 else None for osoba in społecznstwo])

sum_70_t=0
ile_70_t=0
sum_50_bp=0
ile_50_bp=0
sum_40_śl=0
ile_40_śl=0
sum_20_śl_p=0
ile_20_śl_p=0
s70_t = []
s50_bp = []
s50_śl = []
s20_śl_p = []


for osoba in społecznstwo:
    if osoba["wiek"] == 70 and "t" in osoba["imię"].lower():
        s70_t.append(osoba["konto"])
        # sum_70_t += osoba["konto"]
        # ile_70_t += 1
    if osoba["wiek"] >= 50 and not osoba["praca"]:
        s50_bp.append(osoba["konto"])
        # sum_50_bp += osoba["konto"]
        # ile_50_bp += 1
    if osoba["wiek"] < 40 and osoba["ślub"]:
        sum_40_śl += osoba["konto"]
        ile_40_śl += 1
    if osoba["wiek"] < 20 and osoba["ślub"] and osoba["praca"]:
        sum_20_śl_p += osoba["konto"]
        ile_20_śl_p += 1
if len(s70_t) > 0:
    print(f"Średnia 70 lat z literą t w imieniu: {sum(s70_t)/len(s70_t)}")
if len(s50_bp) > 0:
    print(f"Średnia ponad 50 lat bez pracy: {sum(s50_bp)/len(s50_bp)}")
if ile_40_śl > 0:
    print(f"Średnia poniżej 40 lat po ślubie: {sum_40_śl/ile_40_śl}")
if ile_20_śl_p > 0:
    print(f"Średnia poniżej 20 lat po ślubie i z pracą: {sum_20_śl_p/ile_20_śl_p}")
