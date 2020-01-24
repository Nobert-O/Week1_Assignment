# importing the required module
import random


# a function that sorts a randomly generated list
def sort(n):
    lists = []
    for i in range(0,n):
        lists.append(random.randint(0,100))
    mysort = sorted(lists)
    return mysort
print("The list in here are already sorted:",sort(10))
