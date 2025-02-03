# Exercise 73: Show that modifying a variable inside a function does not affect a global variable.
number = 100

def modify_number():
number = 50  # This is a new local variable
print("Inside function, number =", number)

modify_number()
print("Outside function, number =", number)
