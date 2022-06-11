import json

with open('exercise_1.json', 'r') as f:
    data_f = json.load(f)

def get_avg(list):
    return sum(list)/len(list)

nums = 0
c = 0
for k,v in data_f.items():
    c +=1
    only_nums = [x for x in v if type(x) in (int, float)]
    print(f'{k} {get_avg(only_nums):.2f}')
    nums += get_avg(only_nums)
print(f'all_sides {nums/c}')
