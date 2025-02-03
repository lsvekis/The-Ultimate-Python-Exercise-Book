# Exercise 20: Use name mangling to create a private attribute.
class Secret:
def __init__(self, info):
self.__info = info  # Private attribute

def reveal(self):
return self.__info

s = Secret("Hidden message")
print("Revealed secret:", s.reveal())
