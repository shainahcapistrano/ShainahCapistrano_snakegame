# ##use a for loop to go through a file
#
# file = open("./myData/firstFile.txt", "r")
# for line in file:
#     print(line)
# file.close()

#
# This behaves the same as the code below
file = open("./myData/firstFile.txt", "r")
lst = file.readlines()
for line in lst:
    print(line.split())
file.close()
