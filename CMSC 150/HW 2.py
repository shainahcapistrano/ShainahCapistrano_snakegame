# number = int(input("enter a number:"))
# if number % 2 == 0:
#     print(f"number is even")
# else:
#     print(f"number is odd")

# number = int(input("enter a number:"))
# if number > 50:
#     print("positive")
# elif number <= 0 :
#     print("not positive" )

# text = input("enter a word")
# print(len(text))
# if len(text) > 10:
#     print("long")
# elif len(text) == 10:
#     print("ok")
# else:
#     print("short")

# myList = ["Hi", "two", "apple"]
# print(myList)
# myList.append(100)
# print(myList)

# number1 = int(input("Enter an integer "))
# number2 = int(input("Enter an integer "))
# print("Enter 1 to add, 2 to subtract, 3 to multiply, or 4 to divide")
# choice = int(input("What would you like to do:"))


# list1 = [5,2,24,1,7,0]
# list2 = [7,-2,list1,6]
#
#
# print(list1[0] + list2[1])
# print(list2[2][2])
# print(list1[len(list1) - 3])
# print(list1[: 5 : 3])
# print(list1[4 : 2])
# print(list1[:])
# print(list2[ : : -1])
# print(2 in list1)
# print(2 in list2)
# print(2 in list2[2])

# list = [1,2,4,10,19]
# sum = 0
# for number in list:
#         sum = sum + number
# print(sum)

# list = [1, 2, 4, 10, 19]
# odd = ([odd for odd in list if odd % 2 == 1])
# print(sum(odd))

# for x in range(8):
#     print(x, end = " ")
#
# for a in range(3,6):
#     print(a, end = " ")
#
# for y in range(1,9,3):
#     print(y, y+2,end = ", ")

# for element in range(4):
#     print("element", end = " ")
#
# for element in range(12, 3, -2):
#     if (element % 3 == 0):
#         print(element, end = " ")

# a = [1, 4, 2, 3, 18, 7, 3, 4]
# def return_odd_position_element(list_a):
#     x = []
#     for i in range(1,len(list_a),2):
#         x.append(a[i])
#     return x
# odd_element_list = return_odd_position_element(a)
# print(sum(odd_element_list))
#
# for i in range(0,21):
# 	print(2**i)
#
# number1 = int(input("Enter an integer "))
# number2 = int(input("Enter an integer "))
# print("Enter 1 to add, 2 to subtract, 3 to multiply, and 4 to divide")
# choice = int(input("What would you like to do:"))
# if choice == 1:
#     print(number1 + number2)
# elif choice == 2:
#     print(number1 - number2)
# elif choice == 2:
#     print(number1 * number2)
# elif choice == 2:
#     print(number1 / number2)
# else:
#     print("invalid selection")
#
# number = 0
# for item in range(100, 999):
#     if item % 7 == 0 and item % 3 == 0:
#         number += 1
# print(number)
#
# import random
# list = ["Nothing is impossible to a willing heart","Don't pursue happiness- create it","The real kindness comes from within you","Big journeys begin with a single step","Delight the world with compassion, kindness and grace"]
# print(random.choice(list))
#
# input1 = ("yes")
# while input1 == ("yes"):
#     print(random.choice(list))
#     input1 = input("Do you want another fortune?")