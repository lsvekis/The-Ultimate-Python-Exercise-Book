# Exercise 45: Demonstrate mutable default parameter issue.
def append_item(item, lst=None):
if lst is None:
lst = []
lst.append(item)
return lst

print("First call:", append_item(1))
print("Second call:", append_item(2))
