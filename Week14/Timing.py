import time
total = 0
start = time.time()
for number in range(10000000):
    total += number
end = time.time()

print("Time taken is ", end - start)
