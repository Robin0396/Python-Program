import random

test_list = []
for number in range(1,25):
    test_list.append(random.randint (1,10))
print(f'The list of the number is: ')
for i in range (len(test_list)):
    print(test_list[i], end= ' ')
print(f'\nThe sum of all items in the list is: {sum(test_list)}')

