with open('hr_system.txt') as hr_data:
    for info in hr_data:
        splitted_info = info.split()

        names = splitted_info[0]
        job = splitted_info[2]
        id_number = splitted_info[1]
        salary = float(splitted_info[3])
        #calculating the paycheck when they are paid twice in a month
        if job == 'Engineer':
          paycheck = (salary/12)/2 + 1000
        else:
          paycheck = (salary/12)/2

        print(f'{names} (ID:{id_number}), {job} - ${paycheck:.2f}')