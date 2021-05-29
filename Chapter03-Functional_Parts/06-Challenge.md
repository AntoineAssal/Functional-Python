# The Challenge to solve
Assume we have this code that uses what we learned to calculate salaries and compare them.
```py
from functools import reduce

employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]

def is_developer(employee):
    return employee['job_title'] == 'developer'

def is_not_developer(employee):
    return employee['job_title'] != 'developer'

developers = list(filter(is_developer, employees))
non_developers = list(filter(is_not_developer, employees))

def get_salary(employee):
    return employee['salary']

developer_salaries = list(map(get_salary, developers))
non_developer_salaries = list(map(get_salary, non_developers))

def get_sum(acc, x):
    return acc + x

total_developer_salaries = reduce(get_sum, developer_salaries)
average_developer_salary = total_developer_salaries / len(developer_salaries)

total_non_developer_salaries = reduce(get_sum, non_developer_salaries)
average_non_developer_salary = total_non_developer_salaries / len(non_developer_salaries)

print(average_developer_salary)
print(average_non_developer_salary)
```
The challenge is to rewrite the code to do the same thing using list comprehensions ONLY (except reduce).

My full solution is [here](06-Challenge.py)
```py
developer_salaries = [get_salary(emp) for emp in employees if is_developer(emp)]
non_developer_salaries = [get_salary(emp) for emp in employees if is_not_developer(emp)]
```