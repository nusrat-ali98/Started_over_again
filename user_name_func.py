import json

def get_stored_username():
    file_name="update_user.txt"
    try:
        with open(file_name) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Hello "+username+"!")
    else:
        username = input("What is your name? ")
        file_name="update_user.txt"
        with open(file_name, "w") as f:
            json.dump(username, f)
            print("Next time we will remember you "+username+".")

greet_user()

