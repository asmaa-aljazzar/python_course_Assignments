class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#calculate the length of string
print (bcolors.HEADER + "length of banana: " + bcolors.ENDC)
length = len ("banana")
print (length)

print ("\n")

# check if subtext is in the text
print (bcolors.HEADER + "Check if work [nana] is in [banana]" + bcolors.ENDC)
print ("nana" in "banana")

print ("\n")

# check if subtext is in not the text
print (bcolors.HEADER + "Check if work [nana] is not in [banana]"  + bcolors.ENDC)
print ("nana" not in "banana")

print ("\n")

print (bcolors.HEADER + "Print all characters in banana"  + bcolors.ENDC)
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

print (bcolors.HEADER + "Slice from index 2 into 5" + bcolors.ENDC)
print (b[2:5]) # llo
print ("\n")

print (bcolors.HEADER + "Slice from index 0 into 5" + bcolors.ENDC)
print (b[:5]) # start from 0
print ("\n")

print (bcolors.HEADER + "Slice from index 2 until end" + bcolors.ENDC)
print (b[2:]) # to the end of the string
print ("\n")

print (bcolors.HEADER + "Slice from index 2 until end by jump 2 steps each time" + bcolors.ENDC)
print (b[2::2]) # two steps
print ("\n")


print (bcolors.HEADER + "Slice from index -3 to -5 [from the right to the left]" + bcolors.ENDC)
print (b[-5:-2]) # from the right to the left
print ("\n")

print (bcolors.HEADER + "Make the text upper" + bcolors.ENDC)
print (b.upper())
print ("\n")

print (bcolors.HEADER + "Make the text lower" + bcolors.ENDC)
print (b.lower())
print ("\n")

print (bcolors.HEADER + "Delete Spaces at start and end" + bcolors.ENDC)
b = "     Hello, World!     "
print ("Delete: " + b.strip())
print ("\n")

print (bcolors.HEADER + "Replace Between two characters" + bcolors.ENDC)
b = "Hello, World!"
print ("Replace: " + b.replace('o', 'S'))
print ("\n")
