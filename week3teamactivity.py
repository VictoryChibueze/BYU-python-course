grade_percent = float(input('What is your your grade percentage:'))

if grade_percent >= 90:
    grade = 'A'
   
elif grade_percent >=80:
    grade = 'B'
   
elif grade_percent >= 70:
    grade = 'C'
elif grade_percent >=60:
    grade = 'D'
else:
    grade = 'F'
print(f'Your grade is {grade} ')

