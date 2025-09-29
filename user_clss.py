class User():
    def __init__(self, fname , lname , age , qualification ):
        self.first_name = fname
        self.last_name = lname
        self.age = age
        self.qualification = qualification
        self.login_attempts = 0



    def describe_user(self):
        print("My name full name  "+ self.first_name.title() + self.last_name.title() +
              ".\nI am " + str(self.age) + " years old. \nMy qualification is " + self.qualification.title() )

    def greet_user(self):
        print("Welcome to our platform sir "+self.first_name.title() )

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)


    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

user = User("aamir", "ali", 24 , "bachelors")

user.greet_user()
user.describe_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()

user.increment_login_attempts()


class Privelage():
    def __init__(self, privilage=["you are out"]):
        self.privilage = privilage

    def show_privelage(self):
            for privel in self.privilage:
                print(privel)

lst = Privelage(["add to anyone", "remove anyone", "give promotion to anyone"])

class Admin(User):
    def __init__(self,fname,lname,age,qualification):
        super().__init__(fname,lname,age,qualification)
        self.privilega = Privelage()



admin1 = Admin("aamir", "ali", 24 , "bachelors")


admin1.privilega.show_privelage()


