# Exercise 67: Show that local variables are created and destroyed with each function call.
def count_call():
call_count = 0
call_count += 1
print("Call count:", call_count)

count_call()
count_call()
