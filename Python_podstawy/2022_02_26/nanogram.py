def CountHor(str):
    counter = 0
    storage = []
    for a in str:
        if a == "X":
            counter += 1
        elif counter > 0:
            storage.append(counter)
            counter = 0
        else:
            continue
    if counter > 0:
        storage.append(counter)
    counter = 0
    return storage

def CountVer(list):
    counter = 0
    storage = []
    for a[x] in list:


string = "XXX X  XXXXXXXXX  XX"
rys = ["X X X"," X X ","  X  "," X X ","X X X"]
for r in rys:
    print(CountHor(r),r)



# print(count(string))
