##write to a file

fileOut  = open("./myData/out.txt", "w")
fileOut.write("This is one string")
fileOut.write("\n")
fileOut.write("This is a second string")
fileOut.close()


##fileOut = open("./myData/out.txt", "w")
##for i in range(4):
##    fileOut.write("Line " + str(i) + "\n")
##fileOut.close()



##lst = ["This is line 1\n", "This is line 2\n", "This is line 3"]
##fileOut = open("./myData/out.txt", "w")
##fileOut.writelines(lst)
##
##fileOut.close()


##Try appending
##fileOut = open ("./myData/out.txt", "a")
##fileOut.writelines(["\nAppend 1\n", "Append 2"])
##fileOut.close()
    
