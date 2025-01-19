from random import choice

# Getting the names of the students
s1 = input('First student: ')
s2 = input('Second student: ')
s3 = input('Third student: ')

# Putting the names into a list
students = [s1, s2, s3]

# Choosing a random student
chosen_student = choice(students)

# Printing the chosen student
print(f'The student chosen is {chosen_student}')
