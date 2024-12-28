larg = float(input('Enter the width: '))
alt = float(input('Enter the height: '))
area = larg * alt
print('Your wall has the dimensions of {} x {} and its area is {}m²'.format(larg, alt, area))
paint = area / 2
print('To paint this wall, you will need {} liters of paint'.format(paint))
