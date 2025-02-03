# Exercise 31: Use a class method to return the total number of students.
class Student:
total_students = 0

def __init__(self, name):
self.name = name
Student.total_students += 1

@classmethod
def get_total(cls):
return cls.total_students

Student("Oscar")
Student("Pam")
print("Total students (class method):", Student.get_total())
