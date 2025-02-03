# Exercise 57: Define a function that uses a default greeting.
def greet(greeting="Hello", name="World"):
return f"{greeting}, {name}!"

print(greet())
print(greet("Hi", "Sam"))
