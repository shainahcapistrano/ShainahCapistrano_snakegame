import time


def selectionSort(data):

    for index in range(len(data)):

        min = index

        # Find the index'th smallest element
        for scan in range(index + 1, len(data)):
            if (data[scan] < data[min]):
                min = scan

        if min != index: # swap the elements
            data[index], data[min] = data[min], data[index]

    return data

def tester():
   in_list = [14,46,43,27,57,41,45,21,70]
   sorted_list = selectionSort(in_list)
   print(sorted_list)

tester()
