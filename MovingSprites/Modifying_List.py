
def remove_evens(a_list):
    for element in a_list:
        if element % 2 == 0:
            a_list.remove(element)
    return a_list

print(remove_evens([1,2,4,5,7,8,10]))