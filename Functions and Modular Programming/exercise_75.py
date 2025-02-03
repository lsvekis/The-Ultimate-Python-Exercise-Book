# Exercise 75: Return a local variable and examine its lifetime.
def create_message():
message = "This is local"
return message

msg = create_message()
print("Returned message:", msg)
