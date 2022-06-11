import timeit

setup = 'import csv'

code = '''
with open("title_basics.csv", encoding='UTF-8') as f:
    reader = csv.reader(f)
    for idx, row in enumerate(reader):
        print(row)
        if idx == 100:
            break
'''

print(timeit.timeit(stmt=code, setup=setup, number=1))