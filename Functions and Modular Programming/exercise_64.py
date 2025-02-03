# Exercise 64: Demonstrate that a local variable can shadow a global variable.
var = "global"

def shadow():
var = "local"
print("Inside function:", var)

shadow()
print("Outside function:", var)
