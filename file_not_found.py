filename = "aleix.txt"

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    msg = "The file " + filename + " was not found."
    print(msg)
else:
    content = contents.split()
    count = len(content)
    print("The file " + filename + " has " + str(count) + " words.")
