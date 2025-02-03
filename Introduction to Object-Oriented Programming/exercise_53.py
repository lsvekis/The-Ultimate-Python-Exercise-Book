# Exercise 53: Define a method that deletes an attribute.
class Demo:
def __init__(self, value):
self.value = value

def remove_value(self):
del self.value

obj = Demo(10)
print("Value before deletion:", obj.value)
obj.remove_value()
# Uncommenting the next line would cause an AttributeError:
# print(obj.value)
print("Attribute 'value' has been deleted.")
