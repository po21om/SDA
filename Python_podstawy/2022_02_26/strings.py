#
# a = "Raz! Dwa! Trzy!"
# print(type(a))
# print(len(a))
# idx = a.index("!")
# print(idx)
# af = a.find("!")
# print(af)
# ac = a.count("!")
# print(ac)
#
# print(a[5])
#
# pesel = "12323103456" # P - K, NP - M
# print(int(pesel[-2])%2 == 0)
# isFemale = int(pesel[-2])%2 == 0
#
# #print("19"+pesel[0:2], pesel[2:4],pesel[4:6], sep="-") # sep= zmiana separatora (spacja domyslny)
#
# if int(pesel[2]) > 1:
#     print("20" + pesel[0:2], str(int(pesel[2])-2)+pesel[3], pesel[4:6], sep="-")
# else:
#     print("19" + pesel[0:2], pesel[2:4], pesel[4:6], sep="-")
#
# imie = "Tomek"
# print(imie[::2])
# print(imie.upper(),end=" ") # end= zmiana końca lini
# print(imie.lower())
# print(imie.endswith("ek"))
#
# wiek = 30.123456789
#
# print("Cześć nazywam się " + imie + ", mam", wiek, "lat.")
# print("Cześć nazywam się %s, mam %.2f lat." % (imie, wiek)) # %.2f - float do 20go miesca po przecinku
# print("Cześć nazywam się {}, mam {} lat.".format(imie, wiek))
# print(f"Cześć nazywam się {imie}, mam {wiek:.2f} lat.") # f przed tekstem najnowszy, najlepszy
#
# word = "alabasta"
# counter =-1
# for letter in word:
#     counter += 1
#     if letter == "a":
#         print (letter, counter)
#
# napis = "ABAB"
# for idx, val in enumerate(napis):
#     print(idx,val)


raw = "tomek::3/0/::aksloP"
indexy = []
for idx, val in enumerate(raw):
    if val == ":":
        indexy.append(idx)
print(indexy)
# Wyciągnąć dane z raw do 3 zmiennych
# Wypisać "Cześć, nazywam się IMIE, mam WIEK lat, mieszkam w KRAJ"

raw = "piotrek::1/0/0/::aksloP"
indexy = []
for idx, val in enumerate(raw):
    if val == ":":
        indexy.append(idx)


imie = raw[:indexy[0]].capitalize()
wiek = raw[indexy[1]+1:indexy[2]].replace("/","")
kraj = raw[-1:indexy[3]:-1]

print(f"Cześć, nazywam się {imie}, mam {wiek} lat, mieszkam w {kraj}.")
