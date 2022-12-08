# for row in range(4):
#     for count in range(5):
#         print("*", end = " ")
#     print()

# for firstNumber in range(3):
#     for secondNumber in range(2):
#         print("firstNUmber + ", firstnumber, "secondNumber =", secondNumber)
# :
# for secondNumber in range(2):
    # print("firstNUmber + ", firstnumber, "secondNumber =", secondNumber)

# for firstNumber in {0,1,2}:
#     for secondNumber in [0,1]:
#         print("firstNumber = ", firstNumber, "secondNumber = ", secondNumber)
#
#
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20

# for number in range(1,5+1):
#     print(number, end = " ")
# print()
#
# for number in range(1,5+1):
#     print(2 * number, end = " ")
# print()
#
# for number in range(1,5+1):
#     print(3 * number, end = " ")
# print()
#
# for number in range(1,5+1):
#     print(4 * number, end = " ")
# print()
#
# for row in range(1,4+1):
#     for number in range(1,5+1):
#          print(row * number, end = " ")
#     print()

# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# for number in range(1,1+1):
#     print( * number, end = " ")
# print()
# print(1)
# for number in range(1,2+1):
#     print(2 * number, end = " ")
# print()
# for number in range(1,3+1):
#     print(3 * number, end = " ")
# print()
# for number in range(1,4+1):
#     print(4 * number, end = " ")
# print()
# for number in range(1,5+1):
#     print(5 * number, end = " ")
# print()

for row in range(1,5+1):
    for number in range(1,row + 1):
        print(row * number, end = " ")
    print()