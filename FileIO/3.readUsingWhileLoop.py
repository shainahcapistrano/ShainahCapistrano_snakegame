##loop through with a while loop
file = open("./myData/firstFile.txt", "r")
done = False
count = 1
while not done:
    line = file.readline()
    if line != '':
        print("line", count, ":", line)
        #print("line", count, ":", line, end = " ")
        count += 1
    else:
        done = True
file.close()
