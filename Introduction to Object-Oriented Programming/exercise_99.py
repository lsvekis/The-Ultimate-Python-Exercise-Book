# Exercise 99: Override __str__ in different subclasses.
class Person:
def __init__(self, name):
self.name = name

def __str__(self):
return f"Person: {self.name}"

class Student(Person):
def __init__(self, name, major):
super().__init__(name)
self.major = major

def __str__(self):
return f"Student: {self.name}, Major: {self.major}"

p = Person("Zack")
s = Student("Yara", "Computer Science")
print(p)
print(s)
