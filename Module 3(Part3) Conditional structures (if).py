gender = input('Enter your biological gender (male/female)').lower()
hemoglobin_value = float(input('Enter your hemoglobin value (g/l):'))
if gender == 'female':
    if hemoglobin_value < 117:
       print('Hemoglobin value is low.')
    elif 117 <= hemoglobin_value <=155:
        print('Hemoglobin value is normal.')
    else:
        print('Hemoglobin value is high.')
elif gender == 'male':
    if hemoglobin_value < 134:
        print('Hemoglobin value is low.')
    elif 134 <= hemoglobin_value <= 167:
        print('Hemoglobin value is normal.')
    else:
        print('Hemoglobin value is high.')
else:
    print('Invalid gender input')




