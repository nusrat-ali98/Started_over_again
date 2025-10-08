
def count_words(filename):
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


filename = input("Enter file name: ")
count_words(filename)