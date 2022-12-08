def copyFile(inFile, outFile):
    try:
        inputFile = open(inFile, "r")
        contents = inputFile.read()
        inputFile.close()
        outputFile = open(outFile,"w")
        outputFile.write(contents)
        outputFile.close()
        print(copyFile)
    except IOError:
        print("Missing file")

copyFile("test.txt","copytest.txt")
