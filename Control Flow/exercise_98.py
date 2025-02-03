# Exercise 98: Reverse a list by iterating over it.
original_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in original_list:
reversed_list = [item] + reversed_list
print("Reversed list:", reversed_list)
