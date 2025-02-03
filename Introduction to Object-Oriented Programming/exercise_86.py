# Exercise 86: Define a class that adds new attributes in a subclass.
class Employee:
def __init__(self, name):
self.name = name

class Manager(Employee):
def __init__(self, name, department):
super().__init__(name)
self.department = department

m = Manager("Olivia", "Sales")
print(f"Manager {m.name} leads the {m.department} department.")
