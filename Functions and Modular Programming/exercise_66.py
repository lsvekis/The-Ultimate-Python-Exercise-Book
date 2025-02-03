# Exercise 66: Define a function that returns an inner function.
def make_multiplier(factor):
def multiplier(number):
return number * factor
return multiplier

times_three = make_multiplier(3)
print("3 times 5 is:", times_three(5))
