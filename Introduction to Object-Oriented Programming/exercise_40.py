# Exercise 40: Create a class that records its creation time.
import datetime

class Timestamped:
def __init__(self):
self.created_at = datetime.datetime.now()

def get_timestamp(self):
return self.created_at

obj = Timestamped()
print("Object created at:", obj.get_timestamp())
