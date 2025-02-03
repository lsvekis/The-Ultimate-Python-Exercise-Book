# Exercise 50: Concatenate first name and last name stored in an object.
class Person:
def __init__(self, first_name, last_name):
self.first = first_name
self.last = last_name

def full_name(self):
return self.first + " " + self.last

p = Person("Olivia", "Brown")
print("Full name:", p.full_name())
