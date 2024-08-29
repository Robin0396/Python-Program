zander_length = float(input('Enter the length of zander'))
if zander_length >= 42:
    print('Zander meets the required size limit.')
else:
    difference = 42 - zander_length
    print(f'The zander does not meet the required size, Release it back to lake')
    print(f'The fish is {difference:.2f} cm below the required size')
