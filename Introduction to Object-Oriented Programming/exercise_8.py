# Exercise 8: Define a class with a class attribute.
class MyClass:
count = 0

def __init__(self):
MyClass.count += 1

a = MyClass()
b = MyClass()
print("Number of instances:", MyClass.count)
