# Exercise 80: Append items to a global list inside a function.
global_list = []

def add_item(item):
global_list.append(item)

add_item("apple")
add_item("banana")
print("Global list:", global_list)
