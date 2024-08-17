

#initializing variables 

#The variable for the maximum average life expectance 
highest_avg_life_expectancy = -1

#variable for the region with the maximum life expectance
max_country_name = ' '

#variable for the region with the  minimum life expectance
min_country_name = ' '

#The highest average life expectance year
highest_avg_life_expectancy_year = ''

#The variable for the least avearge life expectancy
lowest_avg_life_expectancy = 9999

#The variable for the least avearge life expectancy year
lowest_avg_life_expectancy_year = ' '

#The variable for the code of region or country  with the maximum average life expectancy
max_country_name_code = ''

#The variable for the code of region or country  with the minimum average life expectancy
min_country_name_code = ''

#opening the txt file stored in a folder milestone week6 and initializing it to a variable life data   
with open('milestoneweek6/life-expectancy.txt') as life_data:

    #looping through life data using for lop and initializing each step to row
    for row in life_data:
        
        next(life_data)

        #stripping row of leading and trailing whitespaces and spliting it at every comma 
        splitted_data = row.strip().split(',')
        
        #checking using and an if statement  if length of splitted data is greater than or equal to 3
        if len(splitted_data) >= 3:

            #initialization of each part to a variable
            region_name = splitted_data[0]
            region_code = splitted_data[1]
            life_expectancy_year = splitted_data[2]

            #converting average life expectancy to a float since it was retrieved as a string
            avg_life_expectancy = float(splitted_data[3])
          
          #checking for maximum average life expectancy and which region it occurred as well as the year
            if avg_life_expectancy > highest_avg_life_expectancy:
                max_country_name_code = region_code
                max_country_name = region_name
                highest_avg_life_expectancy_year = life_expectancy_year
                highest_avg_life_expectancy = avg_life_expectancy
         
          #checking for minimum average life expectancy and which region it occurred as well as the year

            elif avg_life_expectancy < lowest_avg_life_expectancy:
                min_country_name = region_name
                min_country_name_code = region_code
                lowest_avg_life_expectancy = avg_life_expectancy
                lowest_avg_life_expectancy_year = life_expectancy_year
  #Displaying the  maximum overall life expectancy
    print(f'The overall maximum life expectancy is: {highest_avg_life_expectancy} from {max_country_name} ({max_country_name_code}) in {highest_avg_life_expectancy_year}')
  
  #Displaying the minimum overall life expectancy  
    print(f'The overall minimum life expectancy is: {lowest_avg_life_expectancy} from {min_country_name} ({min_country_name_code}) in {lowest_avg_life_expectancy_year}')
