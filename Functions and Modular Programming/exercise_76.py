# Exercise 76: Use the nonlocal keyword to modify a variable in an enclosing scope.
def outer_func():
value = "initial"
def inner_func():
nonlocal value
value = "modified"
inner_func()
print("Value after inner function:", value)

outer_func()
