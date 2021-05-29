# Reduce function

The purpose of this function is to allow us to take a list or any other iterable and `reduce` it down to a single value. So for example we could take a list of numbers and `reduce` it down to a sum or an average. Essentially what a `reduce` does is it starts with first element in the list and builds on this initial value in some way until after we've processed all of our elements we end up with the result. In the case of finding the sum of a list of numbers for example, we'd add each element to the initial value. Or if we were trying to find the product of a list of numbers, we'd multiply each element by the initial value and so on. 
```py
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_sum(acc, x):
    return acc + x

sum = reduce(get_sum, numbers_list)
```
```powershell
acc is 0, x is 1
acc is 1, x is 2
acc is 3, x is 3
acc is 6, x is 4
acc is 10, x is 5
acc is 15, x is 6
acc is 21, x is 7
acc is 28, x is 8
acc is 36, x is 9
45
```
