# Exercise 15: Define a function that demonstrates both *args and **kwargs.
def combined_example(*args, **kwargs):
print("Positional arguments:", args)
print("Keyword arguments:", kwargs)

combined_example(1, 2, 3, a="apple", b="banana")
