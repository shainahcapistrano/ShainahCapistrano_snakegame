# def check(num1, num2, num3):
#     if (((num1 + num2) > num3) or ((num2 + num3) > num1)):
#         return False
#     else:
#         return True
#
# print(check(10, 20, 30))
# print(check(50, 10, 30))

#
# def mystery1(theList):
#     if theList == []:
#         return []
#     else:
#         item = min(theList)
#         theList.remove(item)
#         return [item] + mystery1(theList)
#
# print(mystery1 ([2,4,1,3]))

# def mystery2(theList):
#     if theList == []:
#         return []
#     else:
#         return [theList[len(theList) - 1]] + mystery2(theList[0 : len(theList) - 1])
#
# print(mystery2 ([2,4,1,3]))

# list= -2, 2,1,2,3,-4
# def detectPositive(list):
#     for i in list:
#         if list > 0:
#             return True
#         else:
#             return False
#
# print()



def selectionSort(data):
    count = 0
    for index in range(len(data)):
        min = index

        # Find the index'th smallest element
        for scan in range(index + 1, len(data)):
            count += 1
            if (data[scan] < data[min]):
                min = scan

        if min != index: # swap the elements
            data[index], data[min] = data[min], data[index]

    print(count)
    return data

import random

def create_list(list_size):
    out_list = []
    for number in range(list_size):
        out_list.append(random.randrange(1,100))
    return out_list


print(selectionSort(create_list(10000)))








