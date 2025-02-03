import site

print("Site-packages directories:")
for path in site.getsitepackages():
print(path)
