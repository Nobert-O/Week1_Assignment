# importing the required module

import random

# a function that gets the max of a randomly generated list
def max_number(n):
    lists = []
    for i in range(0, n):
        n = random.randint(0,100)
        lists.append(n)
    return lists,"The maximum number in the list is ", max(lists)


print(max_number(10))

