import locale

# Setting BRL Currency 
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

speed = int(input('How fast are you riding? '))
limit = 80
factor = 7

if speed > limit:
    fine = (speed - limit) * factor
    # format fine as coin
    fine_formatted = locale.currency(fine, grouping=True)
    print(f'You got a fine! The value is: {fine_formatted}')
else:
    print('Ok, no fines!')

print('--End--')


