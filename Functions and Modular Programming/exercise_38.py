# Exercise 38: Return the sum of all elements in a list.
def sum_list(lst):
total = 0
for num in lst:
total += num
return total

print("Sum of [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))
