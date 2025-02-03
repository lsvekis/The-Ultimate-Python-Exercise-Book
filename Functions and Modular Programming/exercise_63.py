# Exercise 63: Modify a global variable from inside a function.
count = 0

def increment():
global count
count += 1
print("Inside function, count =", count)

increment()
print("Outside function, count =", count)
