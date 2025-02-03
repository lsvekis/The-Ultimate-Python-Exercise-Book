# Exercise 51: Check if an object meets a certain condition.
class Temperature:
def __init__(self, degrees):
self.degrees = degrees

def is_hot(self):
return self.degrees > 30

temp = Temperature(35)
print("Is it hot?", temp.is_hot())
