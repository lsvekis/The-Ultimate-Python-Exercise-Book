# Exercise 74: Count vowels using a while loop.
text = "hello world"
vowels = "aeiou"
index = 0
count = 0
while index < len(text):
if text[index] in vowels:
count += 1
index += 1
print("Number of vowels:", count)
