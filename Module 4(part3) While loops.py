def find_min_max():
    numbers = []
    while True:
        user_input = input('Enter a number or press Enter to quit: ')
        if user_input == '':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print('Invalid input. Please enter a valid number. ')
    if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f'The smallest number entered is: {smallest}')
        print(f'The largest number entered is: {largest}')
    else:
        print('No numbers were entered.')
find_min_max()


