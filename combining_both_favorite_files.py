import json

file_name = "fav_number.json"

try:
    with open(file_name) as file:
        data = json.load(file)
except FileNotFoundError:
    fav_num = input("Enter your favorite number: ")
    with open(file_name, "w") as file:
        json.dump(fav_num, file)
        print("Your favorite number has been written successfully")
else:
    print("your favorite number is " + data)
    