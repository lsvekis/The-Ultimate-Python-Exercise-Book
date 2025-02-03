# Exercise 5: Instantiate multiple objects of the Person class.
class Person:
def __init__(self, name):
self.name = name

p1 = Person("Bob")
p2 = Person("Carol")
print("Person 1:", p1.name)
print("Person 2:", p2.name)
