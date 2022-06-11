

def small_letter():
    start = 97
    while start <= 122:
        yield chr(start)
        start += 1

sm = small_letter()

for l in sm:
    print(l)

def small_letter_start_end(start_letter, end_letter):
    start = ord(start_letter)
    while start <= ord(end_letter):
        yield chr(start)
        start += 1

smaz = small_letter_start_end('e', 'y')

for l in smaz:
    print(l)

