list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# Set all element in a new list
list3 = list1 + list2

# Copy list
list4 = list1
list5 = list2.copy()

# The new element is a list
list4.append (list1)

# Add one element to the end of the list
list1.append(5)

# Delete all elements
list1.clear()

# List []
# Tuple ()
# Set {} ==> Without repeat

# Cast the list into set to get the unique values
list6 = [5, 2, 5,584, 584, 8, 5, 4] 
setFromList6 = set(list6)

# Dictoinaries: Key[unique] Value
dict1 = {
    "name": "asmaa",
    "age": 25,
    "major": "Computer science"
}
print (dict1)