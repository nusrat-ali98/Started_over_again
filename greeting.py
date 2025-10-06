
name = ""
while name != "q":
    name = input("Please enter your name. If you want to terminate program write 'q' \n")
    file_name = "greet_book.txt"
    with open(file_name, "a") as file:
        file.write("welcome " + name + ", \n")

