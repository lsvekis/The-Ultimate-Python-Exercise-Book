# Exercise 58: Create a class method to return a formatted class info.
class App:
version = "1.0.0"

@classmethod
def get_version(cls):
return f"App version: {cls.version}"

print(App.get_version())
