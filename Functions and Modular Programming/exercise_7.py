# Exercise 7: Define two functions; one calls the other.
def inner():
print("Inside the inner function.")

def outer():
print("Calling the inner function from outer:")
inner()

outer()
