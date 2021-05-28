# Seperation of Data and Functions
Data for our purposes 


## The OOP way
Java:
```java
person = Person("Abel", 31);
person.increase_age();
person.change_name("Aubrey");
```
Python:
```py
class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.initials = f'{first[0]}{last[0]}'
```
In both cases the main reason that it's useful to keep data and functions together in the same object/class definition is that this allows us to interact with the member variables of an object without touching them directly. When an instance of this class is first created, the initials are set properly. But now if we allow programmers to change these properties directly, they have to remember to reset initials every time they change either first name or last name, which they're almost certain to forget somewhere. And this introduces bugs into the program. 

The usual solution to this is to make variables private and only allow them to be changed through specific functions with the authorization to do so. (Private variable is marked with `__` in python)

```py
class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.initials = f'{first[0]}{last[0]}'

    def set_first_name(new_name):
        self.__first_name = new_name
        self.__initials = f'{new_name[0]}{self.__last_name[0]}'

```


 In functional programming, however, the data is never changed and therefore remains a constant source of truth, provided of course that developers are disciplined enough not to change it. So then in functional programming, if we want to transform the data in some way, such as changing someone's name, we simply define a new constant that represents that updated data. We then use this updated constant in all our future calculations, knowing exactly what data it represents. So let's take a look at a  classic example of creating a simple to-do list program that helps people keep track of tasks they need to complete. So here's what an object-oriented approach to this program might look like. First, we'd create a to-do item class that contains properties such as name and completed, as well as functions such as change name or mark as done. And then we might have another class called to-do list, which contains a list of to-do items as well as functions for adding or removing items or sorting them in different ways. 
 ```py
 class TodoItem:
     ...
     def change_name(new_name):
         self.name = new_name
     def mark_done():
         self.completed = True
 class TodoList:
     ...
     def addItem(item):
         self.items.append(item)
     def removeItem(index):
         ...
```
 In functional programming on the other hand, we'd keep the data and functions separate. Instead of wrapping up our data's properties as member variables inside classes, we usually just represent data using constructs such as lists or dictionaries. So for this program, we might have a list of dictionaries, each of which represents a to-do item with name and completed properties. And then separate from this data, we define the functions for working with our data, such as getting all the completed to-do items in a list.
```py
todo_item_1 = {
    'name' : "learn about lambdas and FP",
    'completed' : False,
}
todo_item_2 = {
    'name' : "get a good grade in AI class",
    'completed' : False,
}

todo_list = [ todo_item_1, todo_item_2 ]

def get_completed_items(todo_list):
    ...
``` 