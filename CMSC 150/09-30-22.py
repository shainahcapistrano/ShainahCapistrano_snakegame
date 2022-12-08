# # def add_negatives(list):
# #     total = 0
# #     index = 0
# #     while index < len(list):
# #         if list[index] < 0:
# #             total += list[index]
# #         index += 1
# #     return total
# #
# # print(add_negatives([10,-5,6,7,-1]))
# #
# # def my_split(my_string):
# #     accum_list = []
# #     for character in my_string:
# #         accum_list.append(character)
# #     return accum_list
# #
# # print(my_split("Hello"))
#
#
# # any algo
# def any_greater_n(list, minimum_age):
#     for age in list:
#         if age >= minimum_age:
#             return False
#     return True
# #
# # all algo
# def all_greater_n(list, minimum_age):
#     for age in list:
#         if age < minimum_age:
#             return False
#     return True
#
# ages = [40,19,18,6]
# print(all_greater_n(ages, 18))
# print(any_greater_n(ages, 18))

# # how many algo
# def how_many(list, minimum_age):
#     count = 0
#     for age in list:
#         if age >= minimum_age:
#             count += 1
#     return count
#
# # which items have the characteristic
# def which(list, minimum_age):
#     found_list = []
#     for age in list:
#         if age >= minimum_age:
#            found_list.append(age)
#     return found_list


# def find_min(list):
#     smallest = list[0]
#     for number in list:
#         if number < smallest:
#             smallest = number
#     return smallest
#
# ages = [40,19,18,21,6]
# print(find_min(ages))
#
# def find_max(list):
#     largest = list[0]
#     for number in list:
#         if number > largest:
#             largest = number
#     return largest
#
# ages = [40,19,18,21,6]
# print(find_max(ages))

