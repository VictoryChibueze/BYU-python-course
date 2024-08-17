# number = 0

# # Keep looping as long as the number is less than 10
# while number < 10:
#     number = int(input("What is the number? "))

# print("Finished with the loop")    


# Start with the number 1
# number = 1

# # Keep looping as long as the number is less than or equal to 5
# while number <= 10:
#     # Display the number
#     print(f"The number is: {number}")

#     # Update the number to be one more than it was
#     number = number + 1 

# print("Finished with the loop")



# number = float(input('Please type a positive number:'))

# while number < 0:
#     print('Sorry,that is a negative.Please try again.')
#     number = float(input('Please type a positive number:'))

# print(f'The number is: {number:.2f}')

# child_request =input('May I have a piece of candy?').lower() 

# while child_request != 'yes':
#     child_request =input('May I have a piece of candy?').lower()
# print('Thank You')

# for i in range(100, 200, 10):
#     print(i)
    
# colors =["red","blue","green","yellow"]

# for i in colors:
#     print(i)

# for i in range(1,9):
#     print(i)


# for i in range(2,20,2):
#     print(i)

# word = "book"
# number_of_letters = 4

# for index in range(number_of_letters):
#     print(index)

# word = "book"
# number_of_letters = 4

# for index in range(number_of_letters):
#     letter  = word[index]
#     print(f"Index: {index} letter: {letter}")

# dog_name = input("What is your dog's name?")

# letter_count = len(dog_name)
# print(f"Your dog's name has {letter_count} letters")

# print("This is line one.",end = "")
# print("This is line two")

# word = 'Commitment'

# for letter in word:
#     if letter.lower() == 'm':
#         print('M')
#     else:
#         print(letter)

word = 'commitment'
favourite_letter = input("What's your favourite letter:")



# for letter in word:
#     if letter.lower() == favourite_letter.lower():
#         print(letter.upper(),end = '')

#     else:
#         print(letter.lower(),end = '')
    
for letter in word:
    if letter.lower() ==  favourite_letter.lower():
        print('_',end = '')
    else:
        print(letter.lower(),end = '')

