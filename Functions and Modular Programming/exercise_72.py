# Exercise 72: Demonstrate that a parameter can shadow a global variable.
value = "global value"

def shadow_param(value):
print("Inside function, value =", value)

shadow_param("local value")
print("Outside function, value =", value)
