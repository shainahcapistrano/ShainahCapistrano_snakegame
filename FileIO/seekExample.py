##Try seek:


file = open("./myData/firstFile.txt", "r")
for line in file:
    print(line, end = "")
print()
#file.seek(0)
print("Second time reading:", file.read())
file.close()
