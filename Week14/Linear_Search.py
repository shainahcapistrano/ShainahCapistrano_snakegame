# def findItem(inputList, item):
#     initialize index to start of list and any other variables needed

#     As long as we are not at the end of the list and 	we have not found the item

# 	    if value at current index is equal to item
# 		    return the index
#      else return -1

# def findItem(inputList, item):
#     for element in inputList:
#         if element == item:
#             return True
#     return False

def findItem(inputList, item):
    for index in range(len(inputList)):
        if inputList[index] == item:
            return index
    return -1

# lst = [2, 26, 9, 11, 15, 8, 32]
# print(findItem(lst, 2))


