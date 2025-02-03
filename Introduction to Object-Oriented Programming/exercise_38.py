# Exercise 38: Define a class with default values in __init__.
class Employee:
def __init__(self, name="Unknown", salary=0):
self.name = name
self.salary = salary

emp = Employee()
print("Employee:", emp.name, "Salary:", emp.salary)
