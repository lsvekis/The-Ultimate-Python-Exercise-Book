# Exercise 63: Use a class method to create multiple objects from a list.
class Student:
def __init__(self, name):
self.name = name

@classmethod
def create_students(cls, names):
return [cls(name) for name in names]

students = Student.create_students(["Anna", "Ben", "Cara"])
for s in students:
print("Student name:", s.name)
