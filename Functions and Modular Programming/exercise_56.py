# Exercise 56: Use a default parameter computed based on another parameter.
def greet_with_prefix(name, prefix="Mr." if name.startswith("J") else "Ms."):
return f"{prefix} {name}"

print(greet_with_prefix("John"))
print(greet_with_prefix("Alice"))
