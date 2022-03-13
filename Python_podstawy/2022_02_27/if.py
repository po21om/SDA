wiek = 18
ciaza = False

# Alkohol?
if wiek >= 18 and not ciaza:
    print("Możesz pić alkohol.")
else:
    print("Nie wolno Ci pić.")

# Szkoła
if wiek > 24:
    print("Już pracujesz.")
elif wiek > 19:
    print("Jesteś na studiach.")
elif wiek > 14:
    print("Chodzisz do szkoły średniej.")
elif wiek > 6:
    print("Chodzisz do szkoły podstawowej.")
elif wiek > 2:
    print("Chodzisz do przedszkola.")
else:
    print("Siedzisz w domciu.")

# budzet

budzet = "2021;zarobki=3456;wydatki=2345"

rok = budzet[:4]
zarobki = int(budzet[13:17])
wydatki = int(budzet[26:])

print(f"Zarobki roczne: {zarobki*12} w roku {rok}")
print(f"Wydatki roczne: {wydatki*12} w roku {rok}")
oszczednosci = (zarobki-wydatki)*12

if oszczednosci >= 14000:
    print("Możemy jechać na wakacje opcja 1-sza na bogato.")
elif oszczednosci >= 7000:
    print("Możemy jechać na wakacje opcja 2-ga. Teź będzie fajnie.")
else:
    print("W tym roku siedzimy w domu.")

# pizza

pizza1 = "srednica=40cm;cena=40PLN"
pizza2 = "srednica=36cm;cena=32PLN"

pizza1_pow = 3.14*(int(pizza1[9:11])/2)**2
pizza2_pow = 3.14*(int(pizza2[9:11])/2)**2

if pizza1_pow/int(pizza1[19:21]) > pizza2_pow/int(pizza2[19:21]):
    print(f"Bardziej opłaca się pizza nr 1 o śr. {pizza1[9:13]}")
elif pizza1_pow/int(pizza1[19:21]) < pizza2_pow/int(pizza2[19:21]):
    print(f"Bardziej opłaca się pizza nr 2 o śr. {pizza2[9:13]}")
else:
    print("Obie pizze opłacają się tak samo")
# ktora pizza sie bardziej oplaca?