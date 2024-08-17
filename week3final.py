# An adventure game created with python 
#the story line is a rescue adventure of a damsel who was trapped in a deadly jungle consisting of large snakes and bears 
#But also consist of ways of escape and safe haven when in distress

#while loop to keep the game running continously unless terminated
is_playing = True

while ( is_playing):
    
    #prompting the user to know how ready he/she is for the adventure game
    starter = input('You are going into a jungle are ready? START or QUIT:').lower()

    #checking the user reply using an if ..elif ..else block 
    if starter == 'quit':
      is_playing = False
      print('')
    #if the user enters start the game begins 
    elif starter == 'start':
    # the user is prompted of the light source he/she desires
        print('You are walking through a dark forest and and find two items a MATCH and a FLASHLIGHT')

     #light source stored in a variable called pick up
        pick_up = input('Which one do you want to pick up?:').lower()
       #using if ..elif and else statement to check for the reply of the users
        if pick_up == 'flashlight':
          print('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. ')
        #  prompting the user whether to follow or look in a nested if else statement
          flash_input = input('Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?:').lower()
          if flash_input == 'follow':
            flashlight_direction = input('Keep moving and on approaching a junction ,would you take RIGHT or LEFT?:').upper()
            if flashlight_direction == 'LEFT':
              print('You see a bear running very fast after you ..But there is cave opposite and that\'s your safe haven... ')
            elif flashlight_direction == 'RIGHT':
              print('Here is a horse tied on a tree ,Take your ride ....')

          elif flash_input == 'look':
            print('You look into the woods and you saw a helpless damsel,looking injured and cold and on approaching you saw an anaconda ')
            damsel_rescue =  input('Will you RUN or SAVE the damsel:').upper()
            if damsel_rescue == 'SAVE':
              print('Alas!!..You receive a hero\'s crown.')
            elif damsel_rescue == 'RUN':
              print('The Anaconda attacks and kills you ..The end!!')
          else:
            print("Invalid input !!..Enter 'flashlight' or 'look' ")
        
        #elif block executing the user choosing match as a light source
        elif pick_up == 'match':
          print('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out.')
          match_input = input('Do you want to RUN, or HIDE behind a tree?:').upper()
          if match_input == 'RUN':
            print('The large grizzly bear keeps chasing you and you kept running but now exhausted ....')
            match_run_action = input('Here is a tree will you CLIMB or keep RUNNING:').upper()
            if match_run_action == "CLIMB":
              print('The bears keeps at you but could not get you because of the cave like structure of the mighty safe haven tree...The bear walks away..')
              print(' ')
            elif match_run_action == 'RUNNING':
              print('You get tired and unable to run faster as the bear charges at you and kills you..The end!!')
              print(' ')

          elif match_input == 'HIDE':
            print('The grizzly bear keeps sniifing around but can\'t find you...Stay calm...There you sight a beautiful damsel who was also attacked by the bear.')
            print('You signals her to stay calm as the grizzling bear walks away and you head to safety with her.')
            print('Hey there! You are a hero')
          else:
            print("Invalid reply..Enter 'Run' or 'Hide' ")
       #else block for when the response of the user does not suit any of the given options in the prompt   
        else:
            print('Your input is invalid!!.')

            play_again = input('Do you want to play again YES or NO:').lower()
            if play_again == 'yes':
              is_playing
              print(" ")
            elif play_again == 'no':
              print('Game over!')
              is_playing = False
              print(" ")
