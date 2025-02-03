# Exercise 93: Define a class that inherits from two parent classes.
class Flyer:
def fly(self):
return "Flying"

class Swimmer:
def swim(self):
return "Swimming"

class Duck(Flyer, Swimmer):
pass

d = Duck()
print("Duck can:", d.fly(), "and", d.swim())
