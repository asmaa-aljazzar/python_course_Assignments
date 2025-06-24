import pandas as pd

#! Series
data = [10, 20, 30, 40]
labels = ["a", "b", "c", "d"]

series = pd.Series(data, index=labels)
print ("Series")
print (series)
# print (series) == series ==> both will print the series
series

#! DataFrame
data = {
    "Name": ['Alice', 'Bob', 'Charlie'], # Col1
    "Age": [34, 16, 27],                 # Col2
}