##################################################
# Showing how to add numbers by using a lambda   #
# function to define addition                    #
##################################################

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


add = lambda x, y : x+y


print(add(2, 3))

##################################################
# Passing lambda as a function to the map() seen #
# earlier to return double of numbers            #
##################################################

doubled_numbers = list(map(lambda x: x*2, numbers_list))

print(doubled_numbers)

##################################################
# Having a function return a lambda function     #
##################################################


def create_multiplier(a):
    return lambda x: x * a


double = create_multiplier(2)
print(double(6))
