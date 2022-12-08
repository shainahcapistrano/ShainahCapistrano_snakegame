# def test(x):
#     print("x = " + str(x))
#     x = 5
#     print(y)
#     print("x = " + str(x))
#
# y = 6
# test(y)
# print("y =" + str(y))
#
# number = 5
#
# def create_list(number):
#     list1 = []
#     for x in range(number):
#         list1.append(number)
#     # print(list1)
#     return (list1)
#
# create_list(5)

list = [0, 6, 17, 67, 43]
def test_in_range(list):
    for i in list:
        if i > 10 and i < 20:
            return True
    return False

def find_if_all_range(list):
    for i in list:
        if i < 14 or i > 20:
            return False
    return True


my_input = [11, 6, 17, 67, 43]
print(test_in_range(my_input))

