def print_magician(magician):
    for magicians in magician:
        print(magicians)

def great_magician(magician):

    for i in range(len(magician)):
        magician[i] = "the great " + magician[i]
        print(magician[i])

    return magician



magicians = ["Akbar", "potter", "dumbldor"]
new_lst = great_magician(magicians[:])

print_magician(new_lst)
print(magicians)

