imie = "Tomek"
nazwisko = "Kowalski"
przedmiot = "angielski"
zachowanie = "wzorowe"
czerwony_pasek = True
srednia_ocen = 4.78
pasek = ""
if czerwony_pasek == False:
    pasek = "nie "


print(f"Uczeń {imie} {nazwisko}, którego ulubiony przedmiot to {przedmiot}, mimo {zachowanie}go zachowania i średniej {srednia_ocen} {pasek}otrzymał czerwonego paska.")