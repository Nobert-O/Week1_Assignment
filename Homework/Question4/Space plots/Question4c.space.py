# importing the required modules

import random
import matplotlib.pyplot as plt
from memory_profiler import memory_usage
import memory_profiler


used_space = memory_usage()
def maxnumber(n):
    lists = []
    for i in range(0, n):
        n = random.randint(0,100)
        lists.append(n)
    return lists,max(lists)
space = []
inputs = []
for i in range(1,100,1):
    used_space = memory_usage()

    space.append(used_space)
    inputs.append(i)
# these are the matplot properties I used to plot the graphs
plt.plot(inputs, space)
plt.ylabel("Space Used")
plt.xlabel("Inputs")
plt.title('Spaced Used vs. Changes in Input')
plt.show()
