class bcolor:    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Try to get input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Chooses the operation [+, -, *, /, %, **]: ")
    if (op == '/'):
        # Try to do the operation
        try:
            result = num1 / num2
        except ZeroDivisionError as e:
            print (e)
    elif (op == '+'):
        try:
            result = num1 + num2
        except ZeroDivisionError as e:
            print (e)
    elif (op == '-'):
        try:
            result = num1 - num2
        except ZeroDivisionError as e:
            print (e)
    elif (op == '*'):
        try:
            result = num1 * num2
        except ZeroDivisionError as e:
            print (e)
    elif (op == '%'):
        try:
            result = num1 % num2
        except ZeroDivisionError as e:
            print (e)
    elif (op == '**'):
        try:
            result = num1 ** num2
        except ZeroDivisionError as e:
            print (e)
    else:
        print ("Not supported operator")

except ValueError as e:
    print (e)
try:
    with open ('calculator.txt', 'a', encoding='utf-8') as exepression:
        exepression.write (str(num1))
        exepression.write (' ')
        exepression.write (op)
        exepression.write (' ')
        exepression.write (str(num2))
        exepression.write (' ')
        exepression.write ('=')
        exepression.write (' ')
        exepression.write (str(result))
        exepression.write ('\n')
        print (bcolor.OKGREEN + 'Finishing writhing to [calculator.txt]' + bcolor.ENDC)
except NameError as e:
    print (e)
