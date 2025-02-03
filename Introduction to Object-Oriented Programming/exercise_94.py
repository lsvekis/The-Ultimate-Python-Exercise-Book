# Exercise 94: Override a method that is inherited from multiple classes.
class Flyer:
def move(self):
return "Fly"

class Walker:
def move(self):
return "Walk"

class Bird(Flyer, Walker):
def move(self):
return "Flap and walk"

b = Bird()
print("Bird moves by:", b.move())
