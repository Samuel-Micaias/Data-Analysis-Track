import random

challenge = int(input('Guess the number (between 0 and 5): '))
random_value = random.randint(0, 5)

if challenge == random_value:
    print('You got it!')
else:
    print('Try again! The correct value is:', random_value)

print('--End--')
