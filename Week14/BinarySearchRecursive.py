def binarySearch(myList, target, low, high):
    if high < low:
        return -1
    else:
        midpoint = low + (high - low) // 2
        compareWith = myList[midpoint]
        if target == compareWith:
            return midpoint
        elif target < compareWith:
            return binarySearch(myList, target, low, midpoint-1)
        else: # compareWith < target
            return binarySearch(myList, target, midpoint+1, high)


# search_list = [2,6,7,34,76,123,234,567,677,986]
# print(binarySearch(search_list, 123, 0, len(search_list)-1))