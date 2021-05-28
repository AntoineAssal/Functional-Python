
def double(x):
    return x * 2


def minus_one(x):
    return x - 1


def squared(x):
    return x * x


# Mechanical way of running all these on a given number is:
my_number = 7
my_number = double(my_number)
my_number = minus_one(my_number)
my_number = squared(my_number)
print(my_number) 
# returns 169, ok cool but what if we have more numbers and 10+ functions...

###################################################
# We can store functions in a list instead like   #
# any data type instead, not limited to your funcs#
###################################################
import math

function_list = [
    double,
    minus_one,
    squared,
    math.sqrt
]
my_number = 7

for function in function_list:
    my_number = function(my_number)
print(my_number)