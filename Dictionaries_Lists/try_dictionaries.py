# # animal = ["mammal", "bird", "reptile", "fish"]
# # numberOfSpecies =  [428, 784, 311, 1154]
# #
# # print(animal[3])
# #
# # print(numberOfSpecies[animal.index("reptile")] )
# #
# numberOfSpecies = [ ["mammal", 428], ["bird", 784], ["reptile", 311], ["fish", 1154]]
#
# def find_number_of_animal(animal_type):
#     for element in numberOfSpecies:
# 	    if element[0] == animal_type:
# 		    print(element[1])
#
# find_number_of_animal("reptile")
#
# numberOfSpecies = { "mammal" : 428, "bird" : 784, "reptile" : 311, "fish" : 1154 }
# print(numberOfSpecies["reptile"])
#
# test = {"A" : 1, "B" : 2}
# print(test["B"])
# test["C"] = 3
# print(test)
# test["Z"] = 10
# print(test)
#
#
# if "D" in test:
#     print(test["D"])
# else:
#     print("D not in test")
#     test["D"] = 0
#
#
# print(test)
# test["D"] += 1
# print(test)
#
# print(test["A"] + test["B"])
#
#
# del test["Z"]
# print(test)
# print("Length is ", len(test))

# listOfNum = [10.2, 11.0,2.6, 10.2, 10.2, 12.0, 2.6]
# my_dictionary = {}
# target = 10.2
# print(target in my_dictionary)
#
# my_dictionary[target] = 1
# print(my_dictionary)
# my_dictionary[target] += 1
# print(my_dictionary)

def countNumbers(listOfNum):
    my_dictionary = {}
    for number in listOfNum:
        if number in my_dictionary:
            my_dictionary[number] += 1
        else:
            my_dictionary[number] = 1
    return my_dictionary



listOfNum = [10.2, 11.0, 2.6, 10.2, 10.2, 12.0, 2.6]

print(countNumbers(listOfNum))

# Should return:
# {10.2: 3, 11.0: 1, 2.6: 2, 12.0: 1}



