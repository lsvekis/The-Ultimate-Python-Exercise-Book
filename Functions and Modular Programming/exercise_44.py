# Exercise 44: Define a function with an optional parameter.
def say_message(message, times=1):
for _ in range(times):
print(message)

say_message("Hi there!")
say_message("Repeat this", times=3)
