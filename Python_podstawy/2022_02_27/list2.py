lista = [1,2,["janek","tomek",["Incepcja",2,3]]]
print(lista)
print(lista[1])
print(lista[2])
print(lista[2][1])
print(lista[2][2])
print(lista[2][2][0])
lista2 = lista.pop(2)
print(lista)
print(lista2)
lista3 = lista2.pop(2)
print(lista)
print(lista2)
print(lista3)
lista.extend(lista2)
print(lista)
lista.extend(lista3)
print(lista)