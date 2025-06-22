# A [global] keyword will make the variable value static
# and can modify each time we call the function
 
num = 0

def num_of_customer ():
    global num
    num += 1
    print ("Number of customers now is:", num)

num_of_customer()
num_of_customer()
num_of_customer()
num_of_customer()
num_of_customer()