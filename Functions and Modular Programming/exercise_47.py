# Exercise 47: Define a function that accepts both positional and keyword arguments.
def full_name(first, last, title=""):
if title:
return f"{title} {first} {last}"
else:
return f"{first} {last}"

print(full_name("John", "Doe"))
print(full_name("Jane", "Doe", title="Dr."))
