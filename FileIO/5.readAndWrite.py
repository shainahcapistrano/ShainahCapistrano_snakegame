## add lines in a file
## open file for reading and read in
inFile = open("./myData/out.txt", "r")
contents = inFile.read()
inFile.close()
## manipulate data
contentLst = contents.split("\n")
outFile = open("./myData/out2.txt", "w")
for line in contentLst:
    print(line)
    outFile.write(line + "\n")
    if line != '':
        outFile.write("inserted line\n")
outFile.close()
