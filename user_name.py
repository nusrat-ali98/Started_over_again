name = input("Enter your name: ")

file_object = "user_name.txt"
with open(file_object, "w") as file:
    file.write("hello " + name + ", \n")

    file.write("How are you doing? Sir " + name + "\n")

