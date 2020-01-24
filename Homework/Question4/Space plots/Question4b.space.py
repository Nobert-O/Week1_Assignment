# importing the required modules
import matplotlib.pyplot as plt
import random
from memory_profiler import memory_usage


# a function that generates a list of integers and sorts
def sort(n):
    lists = []
    for i in range(0, n):
        lists.append(random.randint(0, 100))
    mysort = sorted(lists)
    return mysort


# these are lists where I stored my timeused and the different arguments
space = []
inputs = []
# a loop that generates runtime based on ranges
for i in range(1, 100, 10):
    used_space = memory_usage()
    space.append(used_space)
    inputs.append(i)

# these are the matplot properties I used to plot the graphs
plt.plot(inputs, space)
plt.ylabel("Space Used")
plt.xlabel("Inputs")
plt.title('Spaced Used vs. Changes in Input')
plt.show()