# importing the required modules
import string
import random
import timeit
import matplotlib.pyplot as plt


# a funtion that generates a list of strings in lower cases
def String(n):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))

# these are lists where I stored my timeused and the different arguments
worktime = []
work = []
# a loop that generates runtime based on ranges
for i in range(1,100,10):
    plottime = timeit.Timer("i,String(i)", "from __main__ import String, i")
    timeused = plottime.timeit(number=1000)

    worktime.append(timeused)
    work.append(i)

# these are the matplot proberties I used to plot the graphs
plt.plot(worktime,work)
plt.xlabel("Time Used")
plt.ylabel("Inputs")
plt.title('Time Used vs. Changes in Input')
plt.show()