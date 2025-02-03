# Exercise 19: Define a function that uses an inner lambda function.
def apply_operation(a, b, operation):
# operation is a function (e.g., lambda)
return operation(a, b)

result = apply_operation(10, 5, lambda x, y: x - y)
print("Result of subtraction using lambda:", result)
