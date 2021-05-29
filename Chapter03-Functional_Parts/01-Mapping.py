##################################################
# Very basic manipulation. Showing how to return #
# the double of an array/list in another one     #
##################################################

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_list = []

for x in numbers_list:
    doubled_list.append(x*2)

print(doubled_list)

##################################################
# Functional version of the above code.          #
#                                                #
##################################################

def double(x):
    return x*2

print(list(map(double,numbers_list)))