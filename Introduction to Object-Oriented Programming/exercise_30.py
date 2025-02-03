# Exercise 30: Create a class that keeps track of the number of created objects.
class Student:
total_students = 0

def __init__(self, name):
self.name = name
Student.total_students += 1

s1 = Student("Mike")
s2 = Student("Nina")
print("Total students:", Student.total_students)
