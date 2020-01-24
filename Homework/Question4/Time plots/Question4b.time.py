# importing the required modules
import matplotlib.pyplot as plt
import timeit
import random

# a function that generates a list of integers and sorts
def sort(n):
    lists = []
    for i in range(0,n):
        lists.append(random.randint(0,100))
    mysort = sorted(lists)
    return mysort

# these are lists where I stored my timeused and the different arguments
worktime = []
work = []
# a loop that generates runtime based on ranges
for i in range(1,100,10):
    plottime = timeit.Timer("i,sort(i)", "from __main__ import sort, i")
    timeused = plottime.timeit(number=1)

    worktime.append(timeused)
    work.append(i)

# these are the matplot proberties I used to plot the graphs
plt.plot(worktime,work)
plt.xlabel("Time Used")
plt.ylabel("Inputs")
plt.title('Time Used vs. Changes in Input')
plt.show()