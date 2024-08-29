cabin_class = input('Enter the cabin class (Lux, A, B, c): ').upper()
if cabin_class == 'Lux':
    print('Upper deck cabin with balcony.')
elif cabin_class == 'A':
    print('Above the car deck, equipped with a window.')
elif cabin_class == 'B':
    print('Windowless cabin above the car deck.')
elif cabin_class == 'C':
    print('Windowless cabin below the car deck.')
else:
    print('Invalid cabin class')
