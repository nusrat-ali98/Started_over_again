import json

file_name = "numbers.json"
with open(file_name)as file:
    number = json.load(file)
    print(number)