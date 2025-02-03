# Exercise 74: Return the class name using the __class__.__name__ attribute.
class Vehicle:
def get_class_name(self):
return self.__class__.__name__

v = Vehicle()
print("Class name:", v.get_class_name())
