# Map function
Imagine that we want to convert a list of inch measurements into a list of centimeter measurements, or we might have a list of dictionaries representing person data, with name, age, and job attributes, and maybe a lot more data as well, and we just want to convert this data into a list that contains only the people's names. So the typical way of doing this, and the way that many of us first learned how to do it, was to use a for loop to loop through all of the elements in a list, or some other iterable, and push modified elements onto a new one. However, this can very easily lead to bugs, especially as the body of the for loop gets bigger and more complex. 
<img src="https://i.imgur.com/9TaZ0Oi.png">

Python provides a much easier, cleaner, and more functional way of doing this, using its built-in map function that we can call on any list or iterable. The way we use map is by calling it on a list, and passing it some function that we want to apply to each element in the sequence. Map then returns another sequence that contains the return values of that function for each element in the original sequence. 
<img src="https://i.imgur.com/hGl7waK.png">
So, in other words, it takes each element and maps it to the return value of whatever function we're giving it.
<img src="https://i.imgur.com/WFZDypy.png">

Usage example would look something like this. Full commented code [here](01-Mapping.py)!
```py
def double(x):
    return x*2

doubled_list = list(map(double,numbers_list))
print(doubled_list)
```