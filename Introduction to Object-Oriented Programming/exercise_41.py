# Exercise 41: Define a method to return all attribute names and values.
class Data:
def __init__(self, x, y):
self.x = x
self.y = y

def get_attributes(self):
return self.__dict__

d = Data(10, 20)
print("Attributes:", d.get_attributes())
