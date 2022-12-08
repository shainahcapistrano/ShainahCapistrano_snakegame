# class Student:
#     def __init__(self, student_name, id_number):
#         self.student_name = student_name
#         self.id_number = id_number
#
#     def __str__(self):
#         out = self.student_name + "your id number is" + str(self.id_number)
#         return out
#
#
# def tester():
#     karen_id = Student("Karen", 123456)
#     lindsay_id = Student("Lindsay", 678910)
#     print(karen_id)
#     print(lindsay_id)
#
#
# if __name__ == "__main__":
#     tester()

# class Student:
#     def __init__(self, name, ID):
#         self.name = name
#         self.ID = ID
#
#     def student_info(self):
#         return self.name + ", ID:" + str(self.ID)
#
#
# class Club:
#     def __init__(self, club_name, president, secretary):
#         self.clubName = club_name
#         self.president = president
#         self.secretary = secretary
#
#     def __str__(self):
#         return self.clubName + "\npresident: " + self.president.student_info() + "\nsecretary: " + self.secretary.student_info()
#
# def tester():
#     johnBrown = Student("John Brown", 12345)
#     janeSmith = Student("Jane Smith", 98765)
#     mathClub = Club("Math Club", johnBrown, janeSmith)
#     print(mathClub)
#
#
# if __name__ == "__main__":
#     tester()


# class Rectangle():
#     def __init__(self, l, w):
#         self.length = l
#         self.width  = w
#
#     def rectangle_area(self):
#         return self.length*self.width
#
# def tester():
#     newRectangle = Rectangle(12, 10)
#     print(newRectangle.rectangle_area())
#
# if __name__ == "__main__":
#     tester()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class RectangularPrism:
    def __init__(self, rectangle, dep):
        self.base = rectangle
        self.depth = dep

    def __str__(self):
        return "Prism Base length(self.base.length) + Prism Base width(self.base.width) + Prism dept(self.depth)"

    def calculateVolume(self):
        volume = self.base.length * self.base.width * self.depth
        return volume

def tester():
    length = 12
    width = 12
    depth = 12
    baseObj = Rectangle(length, width)
    prism = RectangularPrism(baseObj, depth)
    print(prism.calculateVolume())

if __name__ == '__main__':
    tester()

