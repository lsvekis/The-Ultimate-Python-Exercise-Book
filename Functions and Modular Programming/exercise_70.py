# Exercise 70: Count how many times a function is called using a global variable.
call_counter = 0

def count_calls():
global call_counter
call_counter += 1
print("Function called", call_counter, "times")

count_calls()
count_calls()
