import json

dict = {"a": 1, "b": 12, "c": 18}

with open('example.json', 'w') as f:
    json.dump(dict, f, indent=2)