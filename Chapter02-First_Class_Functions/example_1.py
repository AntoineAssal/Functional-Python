##################################################
# Trivial example to show how this works and get #
# familiar with the syntax of procedural.        #
##################################################

def say_hello(name):
    print(f'Hello {name}')


say_hello_2 = say_hello

say_hello_2('Johnny')


##################################################
# With ternary operators we can use this feature #
# to use functions as data types.                #
##################################################


def fetch_real():
    print("Imagine this runs for a while to fetch over a network...")


def fetch_fake():
    print("Returning fake data")
    return{
        'name': "jane doe",
        'age': 34
    }


ENV = 'dev'

fetch_data = fetch_real if ENV == 'prod' else fetch_fake

data = fetch_data()
