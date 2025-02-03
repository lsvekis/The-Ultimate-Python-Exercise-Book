# Exercise 53: Override default parameters when calling a function.
def greet_person(name="Guest"):
print("Welcome,", name)

greet_person()
greet_person(name="Mark")
