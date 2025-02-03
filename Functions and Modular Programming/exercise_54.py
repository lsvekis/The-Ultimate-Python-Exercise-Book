# Exercise 54: Define a function that accepts any number of arguments and keyword arguments.
def flexible_function(*args, **kwargs):
print("Arguments:", args)
print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, a="alpha", b="beta")
