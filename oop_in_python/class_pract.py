class Animal:
    def __init__(self, name, behavior):
        self.name = name
        self.behavior = behavior

    def eat(self):
        if self.name == "dog":
            print(self.name," Eats meat")
        elif self.name == "cat":
            print(self.name," Eats seeds")

    def sound(self):
        if self.name == "dog":
            print(self.behavior," hawo hawo")
        elif self.name == "cat":
            print(self.behavior," meow meow")

first = Animal("dog","bite")
first.eat()
first.sound()