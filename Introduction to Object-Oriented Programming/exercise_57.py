# Exercise 57: Use a class method to update a class attribute.
class Counter:
count = 0

@classmethod
def increment(cls):
cls.count += 1

Counter.increment()
Counter.increment()
print("Class attribute count:", Counter.count)
