# In the interactive shell:
with open("test.txt", "w") as file:
file.write("Hello, file!")

with open("test.txt", "r") as file:
content = file.read()

content
