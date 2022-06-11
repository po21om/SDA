#lista = ['inni', 'luzak', 'kajak', 'radar', 'kimono']
#palindroms = list(filter(lambda x: x == x[::-1],lista))
#print(palindroms)

#d = [{"b": 1, "a": 6}, {"b": 1, "a": 1}, {"b": 1, "a": 2}, {"b": 1, "a": 3}]
#print(sorted(d, key=lambda x: x["a"]))
#print(sorted(d, key=lambda x: x["a"] * x["b"]))

def likes(names):
    n = len(names)
    print(n)
    names_dict = {
        0: f'no one likes this',
        1: f'{names[0]} likes this',
        2: f'{names[0]} and {names[1]} like this',
        3: f'{names[0]}, {names[1]} and {names[2]} like this',
        4: f'{names[0]}, {names[1]} and {n-2} others like this'
    }
    if n > 4:
        return names_dict[4]
    else:
        return names_dict[n]

likes([])