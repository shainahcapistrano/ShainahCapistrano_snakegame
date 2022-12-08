# ##Plain Read - reads entire file and returns a single string
# # #file = open("e:/myData/firstFile.txt", "r")
# file = open ("./myData/firstFile.txt", "r")
# fileString = file.read()
# file.close()
# print(fileString)
#
#
# ## readlines() returns the entire file but as a list
#
# file = open("./myData/firstFile.txt", "r")
# fileList = file.readlines()
# print(fileList)
# file.close()
#
# ##get a list of strings without the new line character
# file = open("./myData/firstFile.txt", "r")
# fileList2 = (file.read()).split("\n")
# print (fileList2)
# file.close()

#
# #Suppose you really only want to get to one line at a time
try:
    file = open("./myData/firstFile.txt", "r")
    line = file.readline()
    print("1",line)
    file.seek(0)
    file.close()
except:
    print("ooops")
#
# #Suppose you want to loop through the lines in the file manually
# file = open("./myData/firstFile.txt", "r")
# done = False
# while not done:
#    line = file.readline()
#    if line == "":
#        done = True
#    else:
#        print(line)
# file.close()


file = open("./myData/firstFile.txt", "r")
for line in file:
