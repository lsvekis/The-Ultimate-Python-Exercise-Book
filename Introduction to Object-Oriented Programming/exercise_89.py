# Exercise 89: Call the parent class method using super() in an overridden method.
class Animal:
def speak(self):
return "Some generic sound"

class Dog(Animal):
def speak(self):
parent_sound = super().speak()
return parent_sound + " but specifically Woof!"

d = Dog()
print(d.speak())
