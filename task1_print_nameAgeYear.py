import datetime
name = input ("Enter your name: ")
age = int (input ("Enter your age: "))
date = datetime.datetime.now()
year = date.year + (100 - age)
print ("Hi", name, ", you will turn 100 in the year ", year)