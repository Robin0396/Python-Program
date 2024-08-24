#Exercise1
import math
import random
name = input("Enter your name: ")
print(f"Hello, {name}!")
#Exercise2
radius = float(input("What is the radius of the circle?"))
print(f"Area of the circle is {math.pi*radius**2:.2f}")
#Exercise3
rec_length = float(input("What is the length of the rectangle?"))
rec_width = float(input("What is the width of the rectangle?"))
peri_rec = 2*rec_length + 2*rec_width
area_rec =rec_length*rec_width
print(f"The perimeter of the area is: {peri_rec:.1f}")
print(f"The perimeter of rectangle is: {area_rec:.1f}")
#Exercise4
num1 = int(input("Give three integer numbers: "))
num2 = int(input())
num3 = int(input())
print(f"Sum of 3 numbers is {num1+num2+num3}), product {num1*num2*num3}, average {(num1+num2+num3)/3}")
#Exercise5
talent = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))
kg_weight = ((talent*20+pounds)*32 + lots)*0.0133
gr_weight = 1000.0*(kg_weight - int(kg_weight))
print(f"The weight in modern units: \n {int(kg_weight)} kilogram and {gr_weight:.2f} grams")
#Exercise6
print(f"First combination of lock number {random.randint(0, 999):03d}")
four_code = str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) +str(random.randint(1,6))
print("Second combination of lock number " + four_code)




