def create_printer():
    my_fav_number = 7

    def printer():
        print(f'My favorite number is {my_fav_number}')
    return printer


my_printer = create_printer()

my_printer() # -> works has access to the variable

# print(my_fav_number) -> error dont know what this variable is



def create_counter():
    count = 0
    
    def get_count():
        return count

    def increment():
        nonlocal count
        count += 1
    return (get_count, increment)

get_count , increment = create_counter()
# These 2 functions are now the only way to access our 'global' variable count
print(get_count())
increment()
increment()
print(get_count())
increment()
increment()
increment()
increment()
print(get_count())
