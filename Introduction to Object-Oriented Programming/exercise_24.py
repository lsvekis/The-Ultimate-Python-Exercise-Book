# Exercise 24: Define a destructor to see when an object is deleted.
class Temp:
def __init__(self, value):
self.value = value
print(f"Temp object {self.value} created.")

def __del__(self):
print(f"Temp object {self.value} destroyed.")

temp = Temp(1)
del temp
