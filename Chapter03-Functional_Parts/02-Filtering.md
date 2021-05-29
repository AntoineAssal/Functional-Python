# Filter function
Very very similar to `map`. We call it by passing it both a function and an iterable such as a list, tuple or set. The main difference between `filter` and `map`, however, is the purpose of the function that we pass into it. In `map` we pass in a function that **returns a value for each element in an array**. The return value of this function represents what that element becomes in our new array. On the other hand, for `Filter` we pass in a function that returns either `true` or `false` for each element. And what this does is if the function that we pass returns `true` for a given element then that element is included in the `final` result, otherwise it's left out. 

Usage example would look something like this. Full commented code [here](02-Filtering.py)!
```py
def is_even(x):
    return x % 2 == 0


even_list = list(filter(is_even,numbers_list))
print(even_list)
```