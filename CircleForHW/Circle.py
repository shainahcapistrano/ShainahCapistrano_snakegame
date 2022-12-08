import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    # area of a circle is pi * r ** 2
    def calculateArea(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return "Circle with radius " + str(self.radius)


