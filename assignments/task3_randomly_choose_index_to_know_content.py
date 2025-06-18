import random

str = "Success comes to those who work hard."
length = len (str)
index = random.randint (0, length - 1)
print (str)
print ("Randomly selected index: ", index)
print ("Character at this index is: ", str[index])