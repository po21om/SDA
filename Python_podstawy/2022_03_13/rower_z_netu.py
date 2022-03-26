# Pobranie źródła strony przez zrobienia zapytania
import requests
import bs4

def szukaj_rower(zapytanie):
    url = f"https://bike-room.pl/pl/searchquery/{zapytanie}/1/phot/5?url={zapytanie}"

# requests.request('GET','https://bike-room.pl/pl/searchquery/merida/1/phot/5?url=merida')
    r = requests.get(url)

    if "Nie znaleziono produktów" in r.text:
        print("Nie ma roweru :(")
    else:
        print("JEST!")

    soup = bs4.BeautifulSoup(r.text,'html.parser')
    print(soup.body.find(text= "Znaleziono produktów: "))

szukaj_rower("aspre")