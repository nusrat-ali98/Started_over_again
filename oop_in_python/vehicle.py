class vehicle():
    def basic_usage(self):
        print("Basic usage: It is use for transportation")

class car(vehicle):
    def __init__(self):
        print("i am car")
        self.wheel = 4
        self.roof = "Yes"

    def specific_usage(self):
        self.basic_usage()
        print("Specific usage: it is use for office")

class motorbike(vehicle):
    def __init__(self):
        print("i am motorbike")
        self.wheel = 2
        self.roof = "no"

    def specific_usage(self):
        # self.basic_usage()
        print("Specific usage: it is use for motorbike")

c = car()
c.specific_usage()

m = motorbike()
m.basic_usage()
m.specific_usage()