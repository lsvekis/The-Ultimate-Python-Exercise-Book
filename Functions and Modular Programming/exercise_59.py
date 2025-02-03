# Exercise 59: Concatenate first and last names using keyword arguments.
def full_name(*, first, last):
return f"{first} {last}"

print("Full name:", full_name(first="Emily", last="Clark"))
