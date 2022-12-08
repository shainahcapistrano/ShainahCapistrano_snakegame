def binarySearch(myList, target):
    left = 0
    right = len(myList) -1
    while left <= right:
        midpoint = left + (right - left) // 2
        compareWith = myList[midpoint]
        if target == compareWith:
            return midpoint
        elif target < compareWith:
            right = midpoint - 1
        else: # target > compareWith
            left = midpoint + 1
    return -1


search_list = [2,6,7,34,76,123,234,567,677,986]
print(binarySearch(search_list, 123))