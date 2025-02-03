# Exercise 78: Demonstrate that a variable defined at the module level is accessible in functions.
GLOBAL_MESSAGE = "Hello from the module!"

def show_message():
print(GLOBAL_MESSAGE)

show_message()
