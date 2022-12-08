# import address as address


class Person:
#
# Constructor
    def __init__(self, name, address, phone, ssn):
        self.name = name
        self.address = address
        self.phone = phone
        self.ssn =ssn

# Other Methods
# Print Method
    def __str__(self):
      out = self.name + "lives at" + self.address + "with phone"
      out += self.phone + "add SSN" + self.ssn


def tester():
    joel = Person("Joel", "233 2nd Street", "555-555-5555", "111-123-3456")
    print(joel)
#     joel.changeAddress("111 First Street")
#     print(joel)
#
# if __name__ == "__main__":
#     tester()

