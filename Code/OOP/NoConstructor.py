class NoConstructorExample:
    """No Constructor Example"""


    def __str__(self):
        return "Object of class that has no constructor"


def tester():
    my_object = NoConstructorExample()
    print(my_object)



if __name__ == "__main__":
    tester()