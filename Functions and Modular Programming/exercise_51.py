# Exercise 51: Use a default parameter of None for mutable objects.
def add_to_list(item, lst=None):
if lst is None:
lst = []
lst.append(item)
return lst

print("Call 1:", add_to_list("a"))
print("Call 2:", add_to_list("b"))
