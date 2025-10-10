import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
file_name = "username.json"
try:
    with open(file_name)as file:
        data = json.load(file)
except FileNotFoundError:
    name = input("Enter your name: ")
    with open(file_name,"w") as file:
        json.dump(name,file)
        print("we will remember you "+name+". When you will come back")
else:
    print("welcome back "+data)
