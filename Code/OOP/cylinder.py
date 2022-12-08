from circle import *

class Cylinder:


    def __init__(self, base_circle, height):
        self.base_circle = base_circle
        self.height = height

    def calculate_volume(self):
        return self.base_circle.calculate_area() * self.height

    def __str__(self):
        return "Cylinder with base" + self.base_circle + "and height" + str(self.height)

def tester():
    circle1 = circle(2)
    cylinder1 = Cylinder(circle1, 5)
    print(cylinder1)
    print("Volume", cylinder1.calculate_volume())

if __name__ =="__main__":
    tester()