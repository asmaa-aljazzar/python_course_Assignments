#calculate the length of string
print ("length of banana: ")
length = len ("banana")
print (len)

print ("\n")

# check if subtext is in the text
print ("Check if work [nana] is in [banana]")
print ("nana" in "banana")

print ("\n")

# check if subtext is in not the text
print ("Check if work [nana] is not in [banana]")
print ("nana" in "banana")

print ("\n")

print ("Print all characters in banana")
# The x will start from index 0
num = 1
for x in "banana":
    print ("character number",num, ":", x)
    num += 1

print ("\n")

# Slicing
# The upper bound is not included
b = "Hello, World!"
print (b)
print ("\n")

print ("Slice from index 2 into 5")
print (b[2:5]) # llo
print ("\n")

print ("Slice from index 0 into 5")
print (b[:5]) # start from 0
print ("\n")

print ("Slice from index 2 until end")
print (b[2:]) # to the end of the string
print ("\n")

print ("Slice from index 2 until end by jump 2 steps each time")
print (b[2::2]) # two steps
print ("\n")

print ("Slice from index -3 to -5 [from the right to the left]")
print (b[-5:-2]) # from the right to the left
print ("\n")

print ("Make the text upper")
print (b.upper)
print ("\n")

print ("Make the text lower")
print (b.lower)
