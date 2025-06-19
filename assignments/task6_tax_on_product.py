class bcolors:
    HEADER = '\033[95m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

products = {
    "Laptop": 500,
    "Headphones": 80,
    "Mouse": 25,
    "Keyboard": 45
    }

def calculate_tax (price = 0):
    new_price = price * 0.12
    return (new_price)

def apply_discount (price = 0):
    if price > 100:
        new_price = price * 0.10
        return (new_price)
    else:
        return (price)

def final_price (price = 0):
    return ((price - apply_discount (price)) + calculate_tax (price))


name = input ("Enter Product Name: ")

def print_final_price (pname = ""):
    if (pname in products):
        price = products[pname]
        print (bcolors.HEADER + "Product: $", bcolors.YELLOW, pname, bcolors.ENDC)
        print (bcolors.HEADER + "Original Price: $", bcolors.YELLOW, price, bcolors.ENDC)
        print (bcolors.HEADER + "Tax: $", bcolors.YELLOW, calculate_tax(price), bcolors.ENDC)        
        print (bcolors.HEADER + "Discount: $", bcolors.YELLOW, apply_discount(price), bcolors.ENDC)        
        print (bcolors.HEADER + "finalprice: $", bcolors.YELLOW, final_price(price), bcolors.ENDC)        
    
print_final_price (name)