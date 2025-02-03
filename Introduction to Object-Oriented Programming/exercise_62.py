# Exercise 62: Override a class attribute for a specific instance.
class Fruit:
color = "unknown"

apple = Fruit()
apple.color = "red"
print("Apple color:", apple.color)
print("Default Fruit color:", Fruit.color)
