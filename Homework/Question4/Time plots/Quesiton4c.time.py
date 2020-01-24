# importing the required modules

import random
import timeit
import matplotlib.pyplot as plt



def maxnumber(n):
    lists = []
    for i in range(0, n):
        n = random.randint(0,100)
        lists.append(n)
    return lists,\
           max(lists)

# these are lists where I stored my timeused and the different arguments
worktime = []
work = []
# a loop that generates runtime based on ranges
for i in range(1,100,10):
    plottime = timeit.Timer("i,maxnumber(i)", "from __main__ import maxnumber, i")
    timeused = plottime.timeit(number=1000)

    worktime.append(timeused)
    work.append(i)

# these are the matplot proberties I used to plot the graphs
plt.plot(worktime,work)
plt.xlabel("Time Used")
plt.ylabel("Inputs")
plt.title('Time Used vs. Changes in Input')
plt.show()