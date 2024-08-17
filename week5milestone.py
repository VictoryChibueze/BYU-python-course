print("Welcome to shopping Cart")

print()
    
# initializing an empty list where the entered items by the user will appended
shopping_cart = []

entered_action = ''

# A list of prompts that will be displayed for user
display_prompt = ['Add item','View cart','Remove item','Compute total','Quit']

# initializing the sum of the price of items added to the cart by user
price_total = 0


while entered_action != '5':  
    print()

    # Displaying the prompt using a for loop

    print('Please select one of the following:')
    for i in range(len(display_prompt)) :
        print(f'{i+1}. {display_prompt[i]}')

   #prompting the user for action 
    entered_action = input(f'Please enter an action:')

    # if block checking the entered actions
    if entered_action == '1':

    # prompting the user to enter item to be added to cart
        item = input('What item would you like to add?:')

    #prompting for the price of the item added to cart
        price = float(input(f"What is the price of the '{item}':$"))
    
    # appending both item  to empty list 
    
        shopping_cart.append(item)
    
    # displaying to the user item added to the cart 
        print(f"'{item}' has been added to the cart ")

    # if block for functionality that deletes item from the cart
    elif entered_action == '3':

    #Asking the user the item they want to delete
        deleted_item = int(input('Which item would you love to removed:'))

    # Deleting both item and price of item entered by user
        shopping_cart.pop(deleted_item-1)
        
        print('Item removed.')
   #functionality for viewing items in the cart
    elif entered_action == '2':
        for i in range(len(shopping_cart)):
            print(f'{i +1}. {shopping_cart[i]} ')

#    
# Displaying a message to user after they have used the cart
print('Hope you had a nice time shopping ..Enjoy the rest of the day') 