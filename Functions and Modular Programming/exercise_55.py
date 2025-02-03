# Exercise 55: Define a function with a mix of required and default parameters.
def order_params(a, b=2, c=3):
return a + b + c

print("Result (a=5):", order_params(5))
print("Result (a=5, b=4, c=1):", order_params(5, 4, 1))
