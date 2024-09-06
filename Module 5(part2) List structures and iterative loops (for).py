numbers = []
while True:
    user_input = input('Enter a number or press enter to quit: ')
    if user_input == '':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print('Invalid input. Please enter a valid number: ')
numbers.sort(reverse=True)
top_five =numbers[:5]
print('The five greatest numbers in descending order are: ')
print(top_five)
