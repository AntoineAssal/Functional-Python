##################################################
# Very basic manipulation. How to return the     #
# even numbers of an array/list in another one   #
##################################################

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []

for x in numbers_list:
    if (x % 2 == 0):
        even_numbers.append(x)
print(even_numbers)

##################################################
# Functional version of the above code.          #
#                                                #
##################################################


def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, numbers_list)))
