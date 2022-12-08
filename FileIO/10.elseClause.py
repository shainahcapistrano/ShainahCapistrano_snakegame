#Try using an else clause
data = 0
try:
    data = int(input("Enter a number: "))
except ValueError as e:
    print("Value Error:", e)
else:
    data = data +2
    print(data)
