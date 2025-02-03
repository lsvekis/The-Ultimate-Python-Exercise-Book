# Exercise 71: Swap keys and values in a dictionary.
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
print("Inverted dictionary:", inverted)
