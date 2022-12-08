from Book import Book

class Textbook(Book):

    def __init__(self, title, author, copies, subject):
        super().__init__(title, author, copies)
        self.subject = subject


    def calculate_fine(self, days_late):
        return super(). calculate_fine(days_late) + 1


    def __str__(self):
        out = super().__str__() + " with subject " + self.subject
        return out

def tester():
    textbk1 = Textbook("Pyhton for Beginners", "Dawson", 3, "Computer Science")
    book1 = ("Aragon", "Paoline", 2)
    print("Textbook", textbk1.calculate_fine(3))
    print("Book fine", textbk1.calculate_fine(3))
    print(textbk1)

if __name__ == "__main__":
    tester()


