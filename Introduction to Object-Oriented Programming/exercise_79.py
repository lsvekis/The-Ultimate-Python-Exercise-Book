# Exercise 79: Use a class method as an alternative constructor that returns a new object.
class User:
def __init__(self, username):
self.username = username

@classmethod
def guest(cls):
return cls("Guest")

user = User.guest()
print("Guest user:", user.username)
