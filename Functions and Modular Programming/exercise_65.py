# Exercise 65: Define a function inside another function.
def outer():
outer_var = "outer"

def inner():
inner_var = "inner"
print("Inner variable:", inner_var)
print("Access outer variable:", outer_var)

inner()
# inner_var is not accessible here

outer()
