##Handle different kinds of exceptions

try:
    data = int(input("Enter a number: ")) 
    file = open("myData/test.txt","r")
    data2 = int(file.readline())
    data = data + data2
    file.close()
    print(data)
except ValueError:
    print("Number was not an integer")
except IOError as e:
    print("File could not be opened: ", e)

print("Done now")
