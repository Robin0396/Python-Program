import random
num_dice = int(input('How many dice would you to roll? '))
total_sum = 0
for i in range (num_dice):
    roll = random.randint(1,6)
    total_sum += roll
print(f'The sum of dice is {total_sum}')
