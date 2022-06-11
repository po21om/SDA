import json


with open('example.json','r') as f:
    data_from_file = json.load(f)

print(data_from_file)