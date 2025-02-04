name = str(input('Type your name: '))
name_upper = name.upper()
name_lower = name.lower()
name_without_space = name.strip()
name_count = len(name_without_space)
name_slice = len(name[:7])

# Printing the actual values, not the variable names
print(name_upper)
print(name_lower)
print(name_count)
print(name_slice)
