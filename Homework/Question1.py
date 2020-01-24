# importing all the modules required

import timeit
import random

# a function that sorts a randomly generated list
def sort(n):
    lists = []
    for i in range(0,n):
        lists.append(random.randint(0,100))
    mysort = sorted(lists)
    return mysort

# a loop that calculates the time required for the function to run
for i in range(1):
    time1 = timeit.Timer("i,sort(i)", "from __main__ import sort, i")
    timeused = time1.timeit(number=1000)
    print("The time for the algorithm to be executed is",timeused,"seconds")