from Book import *

class Library(object):


    def __init__ (self,name):
        self.name = name
        self.book_list = []

    def add_books (self,book_object):
        self.book_list.append(book_object)

    def __str__(self):
        out = self.name + "has the following books:" + str(self.book_list)
        for book in self.book_list:
            out += str(book)
        return out

def tester():
    library = Library("Simpson")
    library.add_books(Book("The Legend of Sleepy Hollow", "Irving", 2))
    book1 = Book( "Argon", "Paoline", 2)
    library.add_books(book1)
    print(library)

if __name__ == "__main__":
    tester()