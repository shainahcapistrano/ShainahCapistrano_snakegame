# number_of_numbers = 0
# total = 0
# done = False
# while done == False:
#     number = input("Enter a number or press enter to quit:")
#     if number == "":
#         done = True
#     else:
#         number = int(number)
#         total = total + number
#         number_of_numbers += 1
# if number_of_numbers != 0:
# average = total / number_of_numbers
# print(average)

# def my_len(list):
#     number_of_elements = 0
#     for item in list:
#         number_of_elements += 1
#
# the_list = ["a","b","c"]
# # print(len(the_list))
#
# my_len(the_list)
# my_len([3,5,7,9])
#
# def createGreeting(name):
#     out = "Happy birthday to you! Happy birthday to " + name
#
#     print(out)
#
# createGreeting("Suzy")

# def createGreeting(name):
#     out = "Happy birthday to you! Happy birthday to " + name
#
#     return out
#
# greeting1 = createGreeting("Suzy")
# greeting2 = createGreeting("Stanley")
# print(greeting1 + "yea")
# print(greeting2 + "wohoo")


# def modifiedCreateGreeting(name):
#     out = "Happy birthday to you! Happy birthday to you!" + name + ".\n"
#
#     return out
#
#  def singBirthdaySong(name):
#      mainStr = modifiedCreateGreeting(name)
#      print(mainStr + Happy birthday to you!)

# def wish_happy_birthday(name, age):
#     out_string = name + " happy birthday. You are " + str(age) + " years old"
#     return out_string
#
# print(wish_happy_birthday("Eric", 5))

def add_five(number):
    number += 5
    # print(number)
    return number

x = add_five(10)
print(x)