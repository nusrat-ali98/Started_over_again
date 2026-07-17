import json
book = {}
book["aamir"] = {
    "name" : "Aamir",
    "address": "Via monzambano 17, Verona",
    "number": 3241848061
}

s = json.dumps(book)

with open("book.json", "w") as f:
    f.write(s)

with open("book.json", "r") as f:
    read_json = f.read()

read_json = json.loads(read_json)

print(read_json["aamir"])