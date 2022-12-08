from triangle import *

def tester():
    triangle1 = triangle(10,10)
    print(triangle1)
    print("Area", triangle1.calculate_area())

tester()

def tester():
    circle1 = circle(2)
    cylinder1 = Cylinder(circle1, 5)
    print(cylinder1)
    print("Volume", cylinder1.calculate_volume())

if __name__ == "__main__":
    tester()

