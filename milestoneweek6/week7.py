#list of windspeed to be looped through
wind_speeds = [5,10,15,20,25,30,35,40,45,50,55,60]

#an initialization of the variable thats stores user wish to continue or quit
end_prompt = ''

#function that convert degree celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32        #formular to convert celsius to fahrenheit
    return fahrenheit


#function that loop through wind speed list ,checks if entered temperature is in celsuis or fahrenheit
def run_loop():

    #for loop that iterates windspeed
    for speed in wind_speeds:

        #if elif block to check whether the temperature is in celsius or fahrenheit
        if temp_unit.lower() == 'f':
            print(f'At temperature {inputted_temp:.1f}F, and wind speed {speed} mph, the windchill is: {cal_windchill(speed,inputted_temp):.2f}F')
        #checking whether the entered temperature is in celsius then convert it to fahrenheit
        elif temp_unit.lower() == 'c':
            new_temp = celsius_to_fahrenheit(inputted_temp)
            print(f'At temperature {new_temp:.1f}F, and wind speed {speed} mph, the windchill is: {cal_windchill(speed,new_temp):.2f}F')


#function that calculates windchill by taking temperature and windspeed as inputted parameter
def cal_windchill(windspeed,temp):
    windchill = 35.74 + (0.6215 * temp) - 35.75*(windspeed**0.16) + 0.4275 * temp * (windspeed ** 0.16)  #wind chill formular
    return windchill 
 
#while loop that keeps running until the user quits by entering 'no' in the prompt
while end_prompt != 'no':

    #user temperature input
    inputted_temp  = float(input('What is the temperature: '))
    #prompting the user for temperature unit
    temp_unit = input('Fahrenheit or Celsius (F/C): ')


    run_loop()
    
    print()
   #asking the user whether he/she wishes to end the program
    end_prompt = input('Do you wish to continue (YES/NO): ')




    
    

