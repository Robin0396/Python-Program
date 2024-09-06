import random
def dice_roll_side (num):
    return random.randint(1,num)

num = int(input('How many sides in your dice? '))
while True:
    dice = dice_roll_side(num)
    print(f'Dices eyes are: {dice} ')
    if dice == num:
        break