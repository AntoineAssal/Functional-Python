####################################################
# What are higher order functions? First consider  #
# this naive way of defining our division function #
####################################################

def divide(x, y):
    if y == 0:
        print("Error: can't divide by a zero")
        return
    return x/y
# We want our functions to handle only 1 thing. So divide, divides only.
# Doesn't need to be checking for input type. So now:


def divider(x, y):
    return x/y


def checker(function):
    def safe_version(*args):
        if args[1] == 0:
            print("Error: can't divide by a zero")
            return
        return function(*args)
    return safe_version


divide_safe = checker(divider)
print(divide_safe(10, 5))
divide_safe(10, 0)
