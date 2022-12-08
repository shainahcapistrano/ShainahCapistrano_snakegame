# 103 [27, 76, 101, 98] should return True
#
# 100 [127, 176, 101, 198] should return False
#
# 580 [250, 580, 300] should return True

def test_number(number, list):
    for x in list:
        if x <= number:
            return True
        else:
            return False

# input_list = [27, 76, 101, 98]
# input_number = 103
# print(test_number(input_number, input_list))

input_list = [127, 176, 101, 198]
input_number = 100
print(test_number(input_number, input_list))

input_list = [250, 580, 300]
input_number = 580
print(test_number(input_number, input_list))