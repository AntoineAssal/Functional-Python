# List comprehensions
A convenient and concise way of building lists from other sequences:
```py
>>> x = [i*2 for i in range(4)]   # Create a new list and initialize each slot using a loop
>>> x
[0, 2, 4, 6]
```
We can put whatever expression we want in a list comprehension:
```py
>>> ["%.2f" % (i/3) for i in range(4)]    # Fill each slot with the result of a string formatting operation
['0.00', '0.33', '0.67', '1.00']
```
We can can also filter values from the new list:
```py
>>> [i for i in range(8) if i % 2 == 0]   # Create a list object, but only add a new slot if 'i' is even
[0, 2, 4, 6]
```
We can also create dictionaries (or sets) with list comprehension syntax:
```py
>>> names = ['Jack', 'Jill']
>>> grades = [85, 92]
>>> x = {name: grade for name, grade in zip(names, grades)}   # Create (key, value) from each (name, grade)
>>> x
{'Jack': 85, 'Jill': 92}
```
We can have nested loops:
```py
>>> [(i, j) for i in range(2)
...         for j in range(3)]
[(0, 0), (0, 1), (0, 2),
 (1, 0), (1, 1), (1, 2)]
```

This can be confusing. Gotta remember that the earlier for-loops are the 'outer' ones, as if it were written as:
```py
for i in range(2):
    for j in range(3):
        (i, j)
```