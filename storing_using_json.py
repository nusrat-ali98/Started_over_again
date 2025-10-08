import json

numbers = [1,24,5,23,1542,52,342,2342]

with open("numbers.json","w") as file:
    json.dump(numbers,file)