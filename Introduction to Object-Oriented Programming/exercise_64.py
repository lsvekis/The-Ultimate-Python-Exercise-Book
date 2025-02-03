# Exercise 64: Reset a class attribute using a class method.
class Session:
active_sessions = 0

def __init__(self):
Session.active_sessions += 1

@classmethod
def reset_sessions(cls):
cls.active_sessions = 0

Session()
Session()
print("Active sessions before reset:", Session.active_sessions)
Session.reset_sessions()
print("Active sessions after reset:", Session.active_sessions)
