salary = float(input('Enter your salary: '))
adjustment = float(input('Enter your adjustment percentage: '))
salary_adj = salary + (salary * adjustment / 100)
print('After adjustment, your salary is ${:.2f}'.format(salary_adj))
10