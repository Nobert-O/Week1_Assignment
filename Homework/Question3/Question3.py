# importing the required modules
import string
import random


# a function that changes a randomly generated string of lists into lower cases
def String(n):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))

print(String(20))


# a function that uses the lower() function to convert uppercase values to lower...
def words(n):
    a = n.lower()
    print(a)
words("OKOYE-NOBERT CHUKWUEBUKA VALENTINE ")