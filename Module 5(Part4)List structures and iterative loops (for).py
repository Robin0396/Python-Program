cities = []
for i in range(6):
    city = input(f'Enter the city name {i+1}: ')
    cities.append(city)
print('\nThe cities you entered are:')
for city in cities:
    print(city)