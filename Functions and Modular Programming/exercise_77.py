# Exercise 77: Another example of nonlocal variable modification.
def counter_func():
count = 0
def increment():
nonlocal count
count += 1
return count
return increment

counter = counter_func()
print("Counter:", counter())
print("Counter:", counter())
