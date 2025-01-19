from math import hypot

ca = int(input('Enter the length of the adjacent side: '))
co = int(input('Enter the length of the opposite side: '))
hy = hypot(co, ca)

print('The adjacent side length is {} and the opposite side length is {}. The hypotenuse is {:.2f}.'.format(ca, co, hy))
