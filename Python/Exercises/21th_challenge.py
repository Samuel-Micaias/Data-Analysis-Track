days_located = int(input('How many days did you use the location? '))
kilometers_used = int(input('How many kilometers did you travel? '))
price = (60 * days_located) + (kilometers_used * 0.15)
print('The total amount is ${:.2f}'.format(price))
