# this code works, but there is a smarter way to do it. Check below line 07 
v1 = int(input('Type a value! '))
v2 = v1 - 1
v3 = v1 + 1
print('The result before {} is {} and after is {}'.format(v2, v1, v3))

# smarter way
v1 = int(input('Type a value! '))
print('The result before {} is {} and after is {}'.format(v1 - 1, v1, v1 + 1))
