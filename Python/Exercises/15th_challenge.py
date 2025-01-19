from random import shuffle

# Getting the names of the students
s1 = input('First student: ')
s2 = input('Second student: ')
s3 = input('Third student: ')

# Putting the names into a list
students = [s1, s2, s3]

# Shuffling the list to get a random sequence
shuffle(students)

# Printing the shuffled sequence
print('The presentation sequence is:')
print(students)
