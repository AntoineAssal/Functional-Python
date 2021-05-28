def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def combine_2_and_3(function):
    return function(2, 3)


print(combine_2_and_3(add))
print(combine_2_and_3(subtract))


def combine_names(function):
    return function("ovo", "xo")


def append_with_space(s1, s2):
    return f'{s1} {s2}'


def get_govt_form(first, last):
    return f'{last.upper()}, {first.upper()}'

print(combine_names(append_with_space))
print(combine_names(get_govt_form))
