import math


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return "Circle with radius " + str(self.radius)


def test():
    circle1 = Circle(2)
    print("The area is", round(circle1.calculate_area(),2))
    print(circle1)

if __name__ == "__main__":
    test()