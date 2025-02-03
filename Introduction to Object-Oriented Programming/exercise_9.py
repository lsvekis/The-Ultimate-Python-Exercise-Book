# Exercise 9: Define a class method that accesses a class attribute.
class MyClass:
count = 0

def __init__(self):
MyClass.count += 1

@classmethod
def get_count(cls):
return cls.count

a = MyClass()
b = MyClass()
print("Instance count (via class method):", MyClass.get_count())
