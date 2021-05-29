###################################################
# Lets do everything we did so far using this now #
###################################################
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Mapping
doubled = [x*2 for x in numbers_list]
print(doubled)

# Filtering
evens = [x for x in numbers_list if x % 2 == 0]
print(evens)

# Mapping and Filtering
magic = [x*2 for x in numbers_list if x % 2 == 0]
print(magic)