# Use break to out from infinit loop
# day = 0
# while day != 5:
#     day += 1
#     if (day == 3):
#        continue
#     else:
#         print (day)

friends = ["Rima", "Behan", "Asma", "Besan", "Lara"]
your_name = input ("Enter your name: ")
for x in friends:
    if (x == your_name):
        pass # Do nothing
    else:
        print (x)