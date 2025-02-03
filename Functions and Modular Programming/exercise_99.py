# Exercise 99: Reload a module after making changes.
import importlib
import arithmetic  # Assuming arithmetic.py exists

# (Imagine you modify arithmetic.py externally here)

importlib.reload(arithmetic)
print("Reloaded addition (2+3):", arithmetic.add(2, 3))
