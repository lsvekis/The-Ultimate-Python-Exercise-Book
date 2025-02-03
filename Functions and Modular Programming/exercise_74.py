# Exercise 74: Print the memory id of a variable inside and outside a function.
var = [1, 2, 3]

def print_id():
print("Inside function id:", id(var))

print("Outside function id:", id(var))
print_id()
