# Exercise 68: Simulate a static variable using a default mutable parameter.
def counter(count=[0]):
count[0] += 1
print("Count is:", count[0])

counter()
counter()
counter()
