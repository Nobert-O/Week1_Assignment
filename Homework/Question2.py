# importting the required modules

import random
from memory_profiler  import memory_usage

# a function that finds the max number in a randomly generated list
def maxnumber(n):
    lists = []
    for i in range(0, n):
        n = random.randint(0,100)
        lists.append(n)
    return lists,\
           max(lists)

# calling the memory usage for the function
used_space = memory_usage()
print("The spaced used for the algorithm is",used_space,"MiB")