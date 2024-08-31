def inches_to_centimeters():
    while True:
        inches = float(input('Enter value in inches: '))
        if inches < 0:
            print('Negative value entered. ')
            break
        centimeters =  inches * 2.54
        print (f'{inches} inches is equal to {centimeters} centimeters. ')
inches_to_centimeters()

