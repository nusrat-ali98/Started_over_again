name = input("Enter your name: ")
file_name = "user_name.txt"

with open(file_name, "a") as file:
    file.write("Hello "+name + ", \n" )
    file.write("How are you doing? Sir " + name + "\n")
