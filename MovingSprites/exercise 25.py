def buggyList(theList, n):
    outList = []
    for index in range(len(theList)):
        if index < n:
            outList.append(theList[index])
        elif len(theList)-n <= index:
            outList.append(theList[index])
    return outList

lst = [1,2,3,4,5,6,7,8]
print(buggyList(lst, 2))
print(buggyList(lst, 5))
print(buggyList(lst, 0))