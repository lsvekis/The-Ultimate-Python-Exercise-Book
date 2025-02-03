# Exercise 52: Return self from a method to allow method chaining.
class Builder:
def __init__(self):
self.value = ""

def add(self, text):
self.value += text
return self

def result(self):
return self.value

b = Builder()
final = b.add("Hello ").add("World").result()
print("Chained result:", final)
