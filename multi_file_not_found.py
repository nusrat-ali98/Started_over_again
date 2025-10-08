def count_words(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        count = len(words)
        print("The words in " + filename + " are: " + str(count))

filenames =["cat.txt","dog.txt","random"]
for file in filenames:
    count_words(file)