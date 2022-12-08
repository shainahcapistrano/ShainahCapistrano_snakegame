import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return "Circle with radius" + str(self.radius)

def tester():
    circle1 = circle(2)
    print(circle1)

if __name__ == "__main_":
    tester()