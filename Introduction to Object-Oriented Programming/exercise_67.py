# Exercise 67: Define a class with an instance method and a class method.
class Clock:
timezone = "UTC"

def __init__(self, time):
self.time = time

def display_time(self):
print("Current time:", self.time)

@classmethod
def display_timezone(cls):
print("Timezone:", cls.timezone)

clock = Clock("12:00")
clock.display_time()
Clock.display_timezone()
