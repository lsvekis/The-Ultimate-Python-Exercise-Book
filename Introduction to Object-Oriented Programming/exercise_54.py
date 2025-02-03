# Exercise 54: Return the type of an instance attribute.
class DataHolder:
def __init__(self, data):
self.data = data

def data_type(self):
return type(self.data)

dh = DataHolder([1, 2, 3])
print("Data type:", dh.data_type())
