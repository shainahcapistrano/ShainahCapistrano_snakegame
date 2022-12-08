def count_apples():
    apples = 0
    picked_apples = int(input("Pick some apples: "))
    print("You picked", picked_apples)
    apples += picked_apples
    picked_apples = int(input("Pick some more apples: "))
    print("You picked", picked_apples)
    apples += picked_apples
    print("You have picked", apples, "apples.")

count_apples()