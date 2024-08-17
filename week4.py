#Written by Victory Chibueze for BYU pathway week4 assignment

import random
#list of word for hard level of the game
hard_list = ['heritage','ability','opportunity','hello','basket','able','legislation','index','about','organic', 'communication','incredible','leg','deny','gin','above','lifetime','accept','Olympic','demonstration','hypothesis','lifestyle','indication']
word_list_one = random.choice(hard_list)

#list of word for medium level of the game
medium_list = ['operate','lesson',' economy','father','increase','opposite','dust','fiber','online','library']
word_list_two = random.choice(medium_list)

#list of word for easy level of the game
easy_list = [' basis','onion','open','level','life']
word_list_three = random.choice(easy_list)



# Prompting user for the level they wish to play
game_level = input('Which level do you wish to play(HARD/MEDIUM/EASY):').upper()

#if block for the hard level of the game
if game_level == 'HARD':
    
    #initializing of guess count
    guess_count = 0

    guess = ''
    word_count = len(word_list_one)
   
   #Displaying hint for the user
    print('Your hint is :',end=' ')
    for alphabets in word_list_one:
        alphabets = ' _ '
        print(alphabets,end='')
    
    #checking whether guess is equal to generated word
    while guess != word_list_one:
            
        print()
        hint = ''
       #prompting the user for guess
        guess = input("What is your guess?:").lower()
        #updating guess counter
        guess_count = guess_count + 1
        guess_length = len(guess)
        #Displays a message when guess does not contain the same amount of letters as the generated word
        if guess_length != word_count:
            print('Sorry,the guess must have the same number of letters as secret word.')
        else:
            for i,letter in enumerate(word_list_one):
                if guess[i] == letter:
                    hint += guess[i].upper()
                
                elif guess[i] in  word_list_one:
                    hint += guess[i].lower()
                    
                else:
                    hint += '_'
            print(f'Your hint is:{hint}')
    print('Congratulations! You guessed it...')
    print(f'You guessed it in {guess_count} attempts')

#elif block when user enters medium level
elif game_level == 'MEDIUM':
    
    guess_count = 0

    guess = ''
    word_count = len(word_list_two)
   

    print('Your hint is :',end=' ')
    for alphabets in word_list_two:
        alphabets = ' _ '
        print(alphabets,end='')
    while guess != word_list_two:
            
        print()
        hint = ''

        guess = input("What is your guess?:").lower()
        guess_count = guess_count + 1
        guess_length = len(guess)
        if guess_length != word_count:
            print('Sorry,the guess must have the same number of letters as secret word.')
        else:
            for i,letter in enumerate(word_list_two):
                if guess[i] == letter:
                    hint += guess[i].upper()
                
                elif guess[i] in  word_list_two:
                    hint += guess[i].lower()
                    
                else:
                    hint += '_'
            print(f'Your hint is:{hint}')
    print('Congratulations! You guessed it...')
    print(f'You guessed it in {guess_count} attempts')

#elif block when user enters easy level

elif game_level == 'EASY':
    
    guess_count = 0

    guess = ''
    word_count = len(word_list_three)
   

    print('Your hint is :',end=' ')
    for alphabets in word_list_three:
        alphabets = ' _ '
        print(alphabets,end='')
    while guess != word_list_three:
            
        print()
        hint = ''

        guess = input("What is your guess?:").lower()
        guess_count = guess_count + 1
        guess_length = len(guess)
        if guess_length != word_count:
            print('Sorry,the guess must have the same number of letters as secret word.')
        else:
            for i,letter in enumerate(word_list_three):
                if guess[i] == letter:
                    hint += guess[i].upper()
                
                elif guess[i] in  word_list_three:
                    hint += guess[i].lower()
                    
                else:
                    hint += '_'
            print(f'Your hint is :{hint}')
    #Displays congratulatory  when guess is correc and how many attempts made before right guess
    print('Congratulations! You guessed it...')
    print(f'You guessed it in {guess_count} attempts')
else:
    #Displays warning when invalid level is entered by user
    print('Invalid input!')
    
    
    







