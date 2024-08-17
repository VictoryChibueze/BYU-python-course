# courses_file = open('courses.txt')

# for line in courses_file:
#     print(line)

# courses_file.close()

# with open('courses.txt') as courses_file:
#     for line in courses_file:
#         print(line)

#     print('Goodbye')

# print('The file is closed now')

# colors = "red green blue yellow"

# color_parts = colors.split()

# print(colors)
# print(color_parts)

# for col in color_parts:
#     print(col)

# name = 'Brother Burton     '

# clean_name  = name.strip()

# print(f"---{clean_name}---")
# print(f'---{name}---')

# with open('courses.txt') as courses_file:
#     for line in courses_file:
#         parts = line.split(',')


#         print(line)

# with open('books.txt') as books_file:
#     for file in books_file:
#         clean_file = file.strip()
#         print(clean_file)



# numbers = [42,25,18,83,23,85,38,2]

# largest_so_far = numbers[0]

# for number in numbers:
#     if number > largest_so_far:

#       largest_so_far = number

# print(f'The largest is: {largest_so_far}')


# shopping_cart = [
#    ["Chips" , 2.99],
#    ["Bread", 2.50],
#    ["Milk", 3.19],
#    ["Ice cream", 6.99],
#    ["Cheese", 5.99],
#    ["Candy bar", 0.99]
# ]


# max_price = -1

# for item in shopping_cart:
#    price = item[1]

#    if price >  max_price:
#       max_price = price
# print(f"The maximum price is: {max_price}")

# max_price = -1
# max_product = ""  


# for item in shopping_cart:
#    product_name  = item[0]
#    price = item[1]

#    if price >  max_price:
#       max_price = price

#       max_product = product_name
# print(f"The maximum price is: {max_price}")
# print(f"The product with the maximum price is: {max_product}")


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

least_age = 9999

yougest_person = ''

for name in people:
   #spliting the iterated data from the list
   split_data =  name.split()

   person = split_data[0]

   age = int(split_data[1])

   

   if age < least_age:
      least_age = age

      yougest_person = person
      
print(f'The youngest person is {yougest_person} and is {least_age} years old')
