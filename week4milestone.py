# A welcome statement to the user
print('Welcome to the word guessing game!')
print()

# initializing the secret word 
secret_word = 'ability'

secret_word_length = len(secret_word)
# initializing the guess to an empty string 
guess = ''
# initializing the guess counter to zero which will be updated in the loop
guess_count = 0

print('Your hint is: ',end = '')
# a for loop to itearate and display the hint for the user to be pre informed
for char in secret_word:
    char = ' _ '
    print(char, end='')
# while loop when guess is not equal to the secret word
while secret_word != guess:
    # initializing the hint to update in the for loop
    hint = ''
    print()
    # prompting the user for a guess
    guess = input("What is your guess?:").lower()
    # Updating the guess counter on every guess inputed
    guess_count = guess_count + 1

    guess_length = len(guess)
    if guess_length != secret_word_length:
        print('Your guess is incorrect')
    else:
        #    for loop for looping through the secret word and comparing to the letters of the inputed guess
        for i,letter in enumerate(secret_word):
            if guess[i] == letter:
                hint += guess[i].upper()
                
            elif guess[i] in  secret_word:
                hint += guess[i].lower()
                
            else:
                hint += '_'
    
#informs the user about making incorrect guess
        if  guess != secret_word: 
            print('Your guess is incorrect')

#Displays congratulatory message and how many attempts made before the right guess 
        elif secret_word == guess:
            print('Congratulations! You guessed it')
            print(f'It took you {guess_count} attempt')


#Milestone on wordle game projected written by Victory Chibueze


    


    
    

    
        