# Exercise 39: Return the product of all elements in a list.
def product_list(lst):
product = 1
for num in lst:
product *= num
return product

print("Product of [1, 2, 3, 4]:", product_list([1, 2, 3, 4]))
