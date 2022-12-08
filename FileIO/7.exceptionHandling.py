## Try except

done = False
while not done:
    numStr =input("Enter a non-zero integer, press enter to quit: ")
    if numStr == '':
        done = True
    else:
        try:
         number = int(numStr)
         x = 5/number
        except IOError:
            print("enter a number")
            x = 0
        except ZeroDivisionError:
            print("dont enter 0")
            x = 0
    print(x)
       
        
