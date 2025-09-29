class Resturant():
    def __init__(self, resturant_name, resturant_cuisine):
        self.resturant_name = resturant_name
        self.resturant_cuisine = resturant_cuisine

    def describe_resturant(self):
        print("The name of resturant is "+self.resturant_name.title() +"\nOur resturant servers only " +  self.resturant_cuisine
              + " food." )

    def open_resturant(self):
        print(self.resturant_name.title()+ " resturant always opens at 8am.")

class IceCreamStance(Resturant):
    def __init__(self, resturant_name, resturant_cuisine):
        super().__init__(resturant_name, resturant_cuisine)
        self.flavour = ["vanilla", "Stawberry","chocolate"]

    def print_flavour(self):
        for flavour in self.flavour:
            print(flavour.title())

ice_cream = IceCreamStance("ice cream", "chocolate")
ice_cream.print_flavour()




resturant = Resturant("do_dariya", "Pakistani")
resturant1 = Resturant("CBTL", "Bar")
resturant2 = Resturant("OCL", "fast food")

resturant.describe_resturant()
resturant.open_resturant()

resturant1.describe_resturant()
resturant1.open_resturant()

resturant2.describe_resturant()
resturant2.open_resturant()
