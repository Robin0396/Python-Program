import random
def dice_roll():
    return random.randint(1,6)
while True:
    dice = dice_roll()
    print(f'Dice eyes are: {dice}')
    if dice == 6:
        break