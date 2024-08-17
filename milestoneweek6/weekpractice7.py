#import datetime class from datetime library

from datetime import datetime

import math



# first_name =  'Susan'
# print('Task completed')
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#     print(x)

# print('Task completed')
# print(datetime.datetime.now())   
# print()

# def print_time():
#     print('Task completed')
#     print(datetime.now())
#     print()


# first_name = 'Susan'
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()

# first_name = input('Enter your first name: ')
# first_name_initial = first_name[0:1]

# last_name = input('Enter your last name: ')
# last_name_initial = last_name[0:1]

# print('Your initials are:'  + first_name_initial + last_name_initial)


# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial


# first_name = input('Enter your first name: ')
# first_name_initial = get_initial(first_name)

# last_name = input('Enter your last name: ')
# last_name_initial = get_initial(last_name)

# print('Your initials are :' + first_name_initial + last_name_initial)

# def display_message(message):
#     display_regular = message
#     return display_regular


# user_message = input('What is your message? ')

# print(display_message(user_message))



# def display_message(message):
#     display_upper = message.upper()
#     return display_upper


# user_message = input('What is your message ')

# print(display_message(user_message))



# def display_message(message):
#     display_upper = message.lower()
#     return display_upper


# user_message = input('What is your message ')

# print(display_message(user_message))


#function to compute area 

def compute_area_circle(radius):
    x = math.pi
    area_circle = ( radius**2) * x
    return area_circle


# user_inputted_radius = float(input('What is the radius of the circle: '))

# print(f'The area of the circle is: {compute_area_circle(user_inputted_radius):.2f}')




def compute_area_square(side):
    area_square = side**2
    return area_square


# user_inputted_side = float(input('What is the side of the square: '))
# print(f'The area of the square: {compute_area_square(user_inputted_side):.2f}')

def compute_area_rectangle(length,breadth):
    area_reactangle = length * breadth

    return area_reactangle

# user_inputted_length = float(input('What is the length of the rectangle: '))
# user_inputted_breadth  = float(input('What is the breadth of the rectangle: '))

# print(f'The area of the rectangle: {compute_area_rectangle(user_inputted_length,user_inputted_breadth)}')

# shape = ''

# while shape != 'quit':

#     shape = input('Which do you want to calculate(CIRCLE/RECTANGLE/SQUARE): ').lower()

#     if shape == 'circle':
#         user_inputted_radius = float(input('What is the radius of the circle: '))

#         print(f'The area of the circle is: {compute_area_circle(user_inputted_radius):.2f}')
#     elif shape == 'square':
#          user_inputted_length = float(input('What is the length of the square: '))
      

#          print(f'The area of the rectangle: {compute_area_rectangle(user_inputted_length,user_inputted_length)}')

        
#     elif shape == 'rectangle':
#         user_inputted_length = float(input('What is the length of the rectangle: '))
#         user_inputted_breadth  = float(input('What is the breadth of the rectangle: '))

#         print(f'The area of the rectangle: {compute_area_rectangle(user_inputted_length,user_inputted_breadth)}')

# def display_numbers(x, y):

#     print(x)
# display_numbers(3, 3)


# def display_numbers(x, y):
#     print(x)

# x = 3
# y = 4

# display_numbers(x, y)

# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# display_numbers(x, y)

# print(x)


# 

# def display_numbers(x, y):
#     return 10

# x = 3
# y = 4
# x = display_numbers(x, y)

#  print(x)
# def display_numbers(x, y):

#     print(x)
# display_numbers(4, 3)


# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# display_numbers(x, y)

# print(x)

# def display_numbers(x, y):

#     x = 10

# x = 3

# y = 4

# print(display_numbers(x, y))

# def display_numbers(x, y):

#     print(x)

# x = 3

# y = 4

# display_numbers(y, x)

def display_numbers(x, y):
    return 10

x = 3
y = 4
x = display_numbers(x, y)

print(x)