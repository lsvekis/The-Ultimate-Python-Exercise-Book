# Exercise 71: Create a lambda that captures a variable from the enclosing scope.
def make_adder(n):
return lambda x: x + n

add_five = make_adder(5)
print("5 added to 10 is:", add_five(10))
