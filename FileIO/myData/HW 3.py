# def create_message(str):
#     if (len(str) <= 16):
#         return str
#     return str[0:16]
# message1 = "Hello, How are you"
# message2 = "I am fine"
# print(create_message(message1))
# print(create_message(message2))

# for i in range(1, 20, 3):
#     print(i)
# while i < 20:
#     print(i)
#     i += 3
#
# def addToSquare(number):
#     number += 4**2
#     return number
#
# x = addToSquare(10)
# print(x)

# def isOdd(n):
#     return (n % 5 == 0)
# n = 5
# print("True" if isOdd(n) else "False")

# for number in range(1, 20, 3):
#     number = 1
#     while number < 20:
#         print(number, end=" ")
#     number = number - 3

# total = 1
# count = 1
# n = 5
# while count <= n:
#     total *= count
#     count += 1
# print(total)

# total = 1
# for count in range(1,6):
#     total += count
# print(int(total))

# total = 0
# x = 0
# while x < 100:
#   x += 1
#   total += x
# print(total)

# Display total
# start = 1
# end = 100
# total = 0
# while start <= end:
#     total = total + start
# start = start + 1
# print(str(total))

# def write_evens(name,num):
#     try:
#         file = open(name,'w')
#         i = 0
#         while i <= num:
#             if i % 2 == 0:
#                 file.write(str(i) + " ")
#             i += 1
#     except Exception as e:
#         print(e)
#     write_evens("even_file.txt",20)
#

# import arcade
#
# arcade.open_window(600, 600, "Repeating Shapes")
# arcade.set_background_color(arcade.color.WHITE)
# arcade.start_render()
#
# for x in range(0, 600, 50):
#     print(arcade.draw_rectangle_filled(x, x + 20, 20, 1200, arcade.color.BLUE))
#
# arcade.draw_rectangle_filled(0, 20, 20, 1200, arcade.color.BLUE)
#
# arcade.finish_render()
# arcade.run()

# for row in range(6):
#     for star in range(3):
#         print("*", end = " ")
#     print()
# def readFile(file):
#         file_handle = open(file, 'r')
#         file_name = file_handle.read()
#         file_handle.close()
#         return len(file_name)
#
# print (readFile("input.txt"))

# def readFile(file):
#     try:
#         file_handle = open(file, 'r')
#         file_name = file_handle.read()
#         file_handle.close()
#     except:
#         file_name = ""
#         print("file not found")
#     return len(file_name)


# print (readFile("input.txt1"))


def even(number):
    if number % 2 ==0:
        return True
    else:
        return False
print(even(8))
#
# def list_checker(list1):
#     list2 = []
#     for item in list1:
#         if even(item):
#             list2.append(item)
#     return list2

for row in range(6):
    for star in range(3):
        print("*", end = " ")
    print()