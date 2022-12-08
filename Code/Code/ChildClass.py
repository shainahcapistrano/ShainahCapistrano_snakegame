
from ParentA import *
from ParentB import *

class ChildClass(ParentA, ParentB):


    def __init__(self,x, y, z):
        super().__init__(x)
        super().__init__(y)
        self.z = z

    def printThem(self):
        print("x is", self.x)
        ##print("y is", self.y)
        print("z is", self.z)


def tester():
        variable = ChildClass(1,2,3)
        variable.printThem()
        variable.another()
        print(variable.addValues(1,2))

if __name__ == "__main__":
    tester()


