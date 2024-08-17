
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


#Displaying the computed values to the console
print(f'Meal\'s subtotal: ${meal_subtotal:.2f}')
