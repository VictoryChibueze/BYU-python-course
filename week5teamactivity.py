print('Enter a list of numbers,type 0 when finished.')

numbers = [] 
entered_number = None

total = 0
max_num = 0
min_num =9999999999
while entered_number != 0:
    entered_number = int(input('Enter number:'))
    numbers.append(entered_number)

for num in numbers:
   if num > max_num:
       max_num = num
   
   elif num < min_num and num > 0:
       min_num = num
   total +=num

for num in numbers:
   
   
   if num < min_num and num > 0:
       min_num = num


average = total/len(numbers)

print(f'The sum is:{total}')
print(f'The average is:{average}')
print(f'The largest number is:{max_num}')
print(f'The smallest positive  number is:{min_num}')

sorted_list = sorted(numbers)
print('The sorted list:')
for digits in sorted_list:
    print(digits)

