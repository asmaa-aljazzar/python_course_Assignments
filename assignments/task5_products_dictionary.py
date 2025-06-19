class bcolors:
    HEADER = '\033[95m'
    ENDC = '\033[0m'

products = {
    "Laptop": 500,
    "Headphones": 80,
    "Mouse": 25,
    "Keyboard": 45
    }

print ("\n")
print (bcolors.HEADER + "Price of Mouse" + bcolors.ENDC)
print (products["Mouse"])
print ("\n")

print (bcolors.HEADER + "Products Dictionary" + bcolors.ENDC)
print (products)
print ("\n")