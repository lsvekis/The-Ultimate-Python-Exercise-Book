# Exercise 20: Function with a conditional to decide output
def check_value(x):
if x > 0:
return "Positive"
elif x < 0:
return "Negative"
else:
return "Zero"

print("Check 5:", check_value(5))
print("Check -3:", check_value(-3))
print("Check 0:", check_value(0))
