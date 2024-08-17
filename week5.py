print("Welcome to shopping Cart")

print()
    
# initializing an empty list where the entered items by the user will appended
shopping_cart = []

# initializing an empty list where the entered item price by the user will appended
item_price = []

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
        item = input('What item would you like to add?:').capitalize()

    #prompting for the price of the item added to cart
        price = float(input(f"What is the price of the '{item}':$"))
    
    # appending both item and price to various empty list 
        item_price.append(price)
        shopping_cart.append(item)
        print()
        #displaying to the useer how many items are present in the shopping cart
        print(f'You have {len(shopping_cart)} items in your shopping cart')
        print()
    # displaying to the user item added to the cart 
        print(f"'{item}' has been added to the cart ")

    # if block for functionality that deletes item from the cart
    elif entered_action == '3':

    #Asking the user the item they want to delete
        deleted_item = int(input('Which item would you love to remove:'))

    # Deleting both item and price of item entered by user
        shopping_cart.pop(deleted_item-1)
        item_price.pop(deleted_item-1)
        print('Item removed.')
   #functionality for viewing items in the cart
    elif entered_action == '2':
        for i in range(len(shopping_cart)):
            print(f'{i +1}. {shopping_cart[i]} - ${item_price[i]}')

#    functionality for calculating the total price of items added to the cart
    elif entered_action == '4':
        for amount in item_price:
            price_total += amount
        print(f'The total price of items in the cart is ${price_total}')

# Displaying a message to user after they have used the cart
print('Hope you had a nice time shopping ..Enjoy the rest of the day') 