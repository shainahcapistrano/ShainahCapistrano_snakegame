import random
import time
from Linear_Search import *
##from BinarySearchRecursive import *
from BinarySearchIterative import *



def create_list(n):
    out = []
    for number in range(n):
        out.append(random.randrange(1,100))
    return out


long_list = create_list(5000000)
t1 = time.time()
index = findItem(long_list,102)
t2 = time.time()
print(f"The time taken is {t2-t1}")
print(f"Index is {index}")

t1 = time.time()
long_list.sort()
#index = binarySearch(long_list,102,0, len(long_list)-1)
index = binarySearch(long_list,102)
t2 = time.time()
print(f"The time taken is {t2-t1}")
print(f"Index is {index}")
