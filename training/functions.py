def imcrementalFun (num1 = 5, num2 = 5):
    num1 += 1
    print ("num1", num1)
    print ("num1", num2)
    print ("num1 + num2", num1 + num2,'\n')

imcrementalFun (10, 20)

#* With return value.
def my_function(x = 5):
    return 5 * x

#* Cand use pass inside function.

###* Lamda Function:
x = lambda a : a + 10 # Can do one statement at a time, Can take many arguments.
print (x(5))