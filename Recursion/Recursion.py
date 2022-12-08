def mystery(firstNumber, secondNumber):
    if firstNumber <= secondNumber:
        print(firstNumber, end=" ")
        mystery(firstNumber + 1, secondNumber)

mystery(2,5)