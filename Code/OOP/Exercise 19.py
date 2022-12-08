class Book:

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self. copies = copies

    def change_number_of_copies(self ,update_amount):
        self.copies += update_amount

    def calculate_fine(self, days_late):
         return days_late * .1

    def __str__(self):
        return self.title + " by " + self.author + \
               " with " + str(self.copies) + " copies."


def tester():
    book1 = Book ("Argon", "Paoline", 2)
    book1.change_number_of_copies(4)
    print(book1)


if __name__ == "__main__":
    tester()