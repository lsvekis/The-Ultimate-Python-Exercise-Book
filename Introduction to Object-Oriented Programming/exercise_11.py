# Exercise 11: Define a BankAccount class with deposit and withdraw methods.
class BankAccount:
def __init__(self, owner, balance=0):
self.owner = owner
self.balance = balance

def deposit(self, amount):
self.balance += amount
print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

def withdraw(self, amount):
if amount > self.balance:
print("Insufficient funds!")
else:
self.balance -= amount
print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")

account = BankAccount("Eve", 100)
account.deposit(50)
account.withdraw(30)
