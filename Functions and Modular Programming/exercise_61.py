# Exercise 61: Show that variables defined in a function are local.
def local_scope():
local_var = "I exist only here"
print(local_var)

local_scope()
# The following would cause an error if uncommented:
# print(local_var)
