# Exercise 12: Define a function with a docstring.
def greet_with_doc(name):
"""
Greets the person by name.

Parameters:
name (str): The name of the person.

Returns:
None
"""
print("Hello,", name)

greet_with_doc("Bob")
print(greet_with_doc.__doc__)
