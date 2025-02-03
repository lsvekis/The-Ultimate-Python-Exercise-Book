# Save as simple_class.py:
class Person:
def __init__(self, name):
self.name = name

def greet(self):
return f"Hello, my name is {self.name}."

if __name__ == "__main__":
person = Person("Charlie")
print(person.greet())
