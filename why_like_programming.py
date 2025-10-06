while True:
    description = input("Enter a sentence why you like programming. If you dont want to write anything just click enter ")
    if description == "":
        break
    with open("programming_description.txt", "a") as file:
        file.write(description + "\n")


