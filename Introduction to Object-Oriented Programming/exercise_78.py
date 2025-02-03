# Exercise 78: Reset a class attribute using a method.
class Session:
active = True

@classmethod
def reset(cls):
cls.active = False

print("Session active:", Session.active)
Session.reset()
print("Session active after reset:", Session.active)
