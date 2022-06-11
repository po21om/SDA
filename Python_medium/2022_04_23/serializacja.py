import pickle

data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("Ala ma kota", "Programowanie w pythonie jest super"),
    'c': [False, True, False]
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)