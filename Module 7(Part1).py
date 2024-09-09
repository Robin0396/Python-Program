def get_seasons(month):
    seasons = ('Winter', 'Spring', 'Summer', 'Autumn')
    if month in [12,1,2]:
        return seasons [0]
    elif month in [3,4,5]:
        return seasons [1]
    elif month in [6,7,8]:
        return seasons [2]
    elif month in [9,10,11]:
        return seasons [3]
    else:
        return None

month_number = int(input('Enter the month number 1-12 ):' ))
season = get_seasons(month_number)

if season:
    print(f'The season for the month {month_number} is {season} ')

else:
    print('Invalid number please enter 1-12')
