# Exercise 75: Track instances by name using a class attribute.
class User:
users = []

def __init__(self, name):
self.name = name
User.users.append(name)

@classmethod
def get_users(cls):
return cls.users

User("Sam")
User("Tina")
print("All users:", User.get_users())
