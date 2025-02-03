# Exercise 93: Determine if a string is a palindrome.
text = "radar"
reversed_text = ""
for char in text:
reversed_text = char + reversed_text
if text == reversed_text:
print("Palindrome")
else:
print("Not a palindrome")
