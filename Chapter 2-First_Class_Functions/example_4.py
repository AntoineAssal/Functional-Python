##################################################
# Trivial example here to see how we can have a  #
# function returned by another function          #
##################################################

def create_printer():
    def printer():
        print("Hello functional!")
    return printer


my_printer = create_printer()
my_printer()
####################################################
# Looking at the following code we can already see #
# how repeatable it is. Whats the functional way?  #
####################################################

"""def double(x):
    return x * 2


def triple(x):
    return x * 3


def quadruple(x):
    return x * 4
"""
####################################################
# By using this we eliminate the need for all the  #
# other functions by having a "function factory"   #
####################################################

def create_mutiplyer(a):
    def multiplyer(x):
        return x * a
    return multiplyer

double = create_mutiplyer(2)
triple = create_mutiplyer(3)
quadruple = create_mutiplyer(4)

print(double(5))
print(triple(6))
print(quadruple(7))