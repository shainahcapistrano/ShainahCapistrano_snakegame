class Car:

    # Constructor
    number_of_cars = 0

    def __init__(self, make, model, mpg):
        self.make = make
        self.model = model
        self.mpg = mpg
        Car.number_of_cars += 1

    @staticmethod
    def return_number_of_cars():
        return Car.number_of_cars




    def __str__(self):
        return self.make + " " + self.model + \
             " gets " + str(self.mpg) + " miles to the gallon"

def tester():
    car1 = Car("Dodge", "Challenger", 27)
    car2 = Car("Ford", "Mustang", 20)
    car3 = Car("Ford", "Taurus", 30)
    print("Number of car is", Car.return_number_of_cars())

if __name__ == "__main__":
    tester()