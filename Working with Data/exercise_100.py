# Exercise 100: Combine iteration over a list, tuple, and dictionary.
sample_list = [1, 2, 3]
sample_tuple = ("a", "b", "c")
sample_dict = {"x": 10, "y": 20}

print("Iterating over list:")
for item in sample_list:
print(item)

print("Iterating over tuple:")
for item in sample_tuple:
print(item)

print("Iterating over dictionary:")
for key, value in sample_dict.items():
print(f"{key}: {value}")
