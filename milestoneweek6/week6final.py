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

#while loop switch variable
request_on = 1

#initialization of request year to none
request_year = None

year = []
#variable for summation of average life expectancy
summed_avg_life_expectancy = 0
#expectancy list variable
expectancy_list = []

#expectancy list length variable initialization
expectancy_list_length = 0
#index length variable 
index_length = []

#list variable where countries that are requested are been stored
country_requested = []
#variable for country with maximun expectancy
max_country_requested = ''
#variable for country with minimum expectancy
min_country_requested = ''

#initializtion of variable for  maximun expectancy
max_expectancy_requested = 0
#initializtion of variable for  maximun expectancy
min_expectancy_requested = 999999
#loop count variable
count = 0
#opening the txt file stored in a folder milestone week6 and initializing it to a variable life data   
with open('milestoneweek6/life-expectancy.txt') as life_data:

    #looping through life data using for lop and initializing each step to row
    for row in life_data:

        #stripping row of leading and trailing whitespaces and spliting it at every comma 
        splitted_data = row.strip().split(',')
        
        #checking using and an if statement  if length of splitted data is greater than or equal to 3
        if len(splitted_data) >= 3:

            #initialization of each part to a variable
            region_name = splitted_data[0]    #initilaizing the region to a region name variable

            #appending the region name to a country_requested list
            country_requested.append(region_name)

            region_code = splitted_data[1]    #initilaizing the region code to a region code variable
           
            life_expectancy_year = splitted_data[2]  #
           #appending the life expectancy year to a year list
            year.append(life_expectancy_year)

            #converting average life expectancy to a float since it was retrieved as a string
            avg_life_expectancy = float(splitted_data[3])
            #Appending average life expectancy to expectancy list
            expectancy_list.append(avg_life_expectancy)
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
    print()
    while request_on == 1:
      print()
      request_year = int(input("Enter the year of interest: "))
      #loop count variable
      count +=1
      print()
      
#for loop to itearte the year requested by user 
      for index in range(len(year)):
          if int(year[index]) == request_year:
          
              summed_avg_life_expectancy += float(expectancy_list[index])
              # print(float(expectancy_list[index]))
              index_length.append(expectancy_list[index])
              expectancy_list_length = len(index_length)
#if elif block to determine the max and min life expectancy of the year requested by the user
              if float(expectancy_list[index]) > max_expectancy_requested:
                  max_expectancy_requested = float(expectancy_list[index])
                  max_country_requested = country_requested[index]
                  
              elif float(expectancy_list[index]) < min_expectancy_requested:
                  min_expectancy_requested = float(expectancy_list[index])
                  min_country_requested = country_requested[index]
                  average = summed_avg_life_expectancy /int(expectancy_list_length)
#Displays to the user the average expectancy for country he/she requested and country with max expectancy as well as country with minimum
      print(f'The average life across all countries in {request_year} was {average:.2f}')
      print(f'The max life expectancy was in {max_country_requested} with {max_expectancy_requested}')   
      print(f'The min life expetancy was in {min_country_requested} with {min_expectancy_requested}')

#code block for terminating the loop using counter variable         
      if count ==2:
         #prompts user for an end while counter is equals to 2
         count_prompt = input('Do you wish to continue (YES/NO): ')
         if count_prompt.lower == 'no':
             request_on = 0
             #ends loop while count is equals to 4
      elif count == 4:
          request_on = 0 
         
      
