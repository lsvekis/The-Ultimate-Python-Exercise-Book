# Exercise 52: Define a function that requires keyword-only arguments with defaults.
def make_profile(*, name="Unknown", age=0):
return {"name": name, "age": age}

print("Profile:", make_profile(name="Laura", age=34))
print("Default Profile:", make_profile())
