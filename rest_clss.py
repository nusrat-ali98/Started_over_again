class Resturant():
    def __init__(self, resturant_name, resturant_cuisine):
        self.resturant_name = resturant_name
        self.resturant_cuisine = resturant_cuisine
        self.number_serverd = 0

    def describe_resturant(self):
        print("The name of resturant is "+self.resturant_name.title() +"\nOur resturant servers only " +  self.resturant_cuisine
              + " food." )

    def open_resturant(self):
        print(self.resturant_name.title()+ " resturant always opens at 8am.")


    def set_number_serverd(self, number):
        if number >= self.number_serverd:
            self.number_serverd = number
        else:
            print("Number serverd than not be lower than before")

    def increment_number_serverd(self, new_customer):
        self.number_serverd += new_customer

    def print_serverd(self):
        print(self.number_serverd)


resturant = Resturant("My name", "My qualification")

resturant.set_number_serverd(14)
resturant.increment_number_serverd(15)
resturant.print_serverd()

