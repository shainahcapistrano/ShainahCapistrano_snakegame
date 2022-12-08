# Conditional Loops
# i = 0
# while i < 4:
#     print(i)
#     i = i + 1
#
# x = 20
# while x >= 10:
#     print("hi")
#     x = x - 2

# i = 5
# while i < 10:
#    print(i)
#    i += 2
#
counter = 0
integer1= int(input("Enter an integer: "))
integer2= int(input("Enter an integer: "))
if integer1 < integer2:
   temp = integer1
   integer1 = integer2
   integer2 = temp
while integer1 >= integer2:
    integer1 = integer1 - integer2
    counter += 1

print(counter)
