## Try except

done = False
content = ""
while not done:
    filename =input("Enter a file name to read from: ")
    try:
        inFile = open(filename, "r")
        content = inFile.read()
        
    except IOError:
        print("Invalid file name")
    else:
        done = True
        
    print (content)
