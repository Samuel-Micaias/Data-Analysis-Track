num = int(input('Type a number: '))
u = num // 1    % 10  # Units place
d = num // 10   % 10  # Tens place
c = num // 100  % 10  # Hundreds place
m = num // 1000 % 10  # Thousands place

# Printing the values for each place
print(u)  # Units place
print(d)  # Tens place
print(c)  # Hundreds place
print(m)  # Thousands place
