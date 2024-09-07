import math
def pizza_size(d,price):
    return price/math.pi * (d / 200.) ** 2
p1_diameter = float(input('What is the diameter of the 1st pizza {in cm}?: '))
p1_price = float(input('What is the price of the first pizza {in euro}?: '))
p2_diameter = float(input('Whats is the diameter of the 2nd pizza {in cm}?: '))
p2_price = float(input('What is the price of the 2nd pizza {in euro}?: '))

if pizza_size(p1_diameter,p1_price) < pizza_size(p2_diameter,p2_price):
    print('The first pizza is a good choice! Go for it!')
else:
    print('The second pizza is a good choice! Go for it!')
