def gallon_to_liters (gallon):
    return 3.785 * gallon

while True:
    user_gallon = float(input('How many gallons to convert? '))
    if user_gallon < 0:
        break
    print(f'{user_gallon} gallons are {gallon_to_liters(user_gallon):.1f} liters.')


