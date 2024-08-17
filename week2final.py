print('MEAL CALCULATOR....')

#prompting the user for child meal price
child_meal = float(input('What is the price of a child\'s meal:$'))
#prompting the user for adult meal price
adult_meal = float(input('What is the price of an adult\'s meal:$'))

#prompting the user for number of children and adult presnt respectively
children_number = int(input('What\'s the number children present:'))
adult_number =  int(input('What\'s the number adult present:'))

#prompting the user for sales tax rate 
sales_tax_rate = float(input('Enter the sales tax rate:'))

#Calculating the subtotal of meals respectively and storing in separate variables
child_meal_subtotal = child_meal *children_number
adult_meal_subtotal = adult_meal * adult_number
meal_subtotal = child_meal_subtotal + adult_meal_subtotal

#computing the value of the sales tax
sales_tax_value = meal_subtotal * (sales_tax_rate/100) 

#computing the total cost of the meal
total_cost = meal_subtotal + sales_tax_value

#Displaying the computed values to the console
print(f'Meal\'s subtotal: ${meal_subtotal:.2f}')
print(f'Sales Tax of: ${sales_tax_value:.2f}')
print(f'Total cost of meal: ${total_cost:.2f}')

#prompting the user for tip

tip = float(input('How many percent tip do you care for:'))
print()
print()
#displaying to user tip disclaimer
print('Please bear in mind that this tip is directed to feed a poor child mission...')

tip_value  = total_cost * (tip/100)
#displaying to user tip value
print(f'You just tipped ${tip_value:.2f}..')

#Prompting the user for payment amount
payment_amount = float(input('Enter the payment:$'))

balance = payment_amount - (total_cost +tip_value)

print(f'Your balance is: ${balance:.2f}')

print('HOPE YOU ENJOYED YOURSELF....THANKS FOR PATRONAGE')
