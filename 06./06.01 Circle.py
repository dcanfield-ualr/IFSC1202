"""
You have a file that has the radius of a circle, one per line.
Create a program that performs the following:
Defines a function called "diameter"
Accepts the radius (floating point) as a parameter
Calculates and returns the diameter of the circle, (2 times radius)
Defines a function called "circumference"
Accepts the radius (floating point) as a parameter
Calculates and returns the circumference of the circle, (2 times pi times radius)
Defines a function called "area"
Accepts the radius (floating point) as a parameter
Calculates and returns the area of the circle, (pi times radius squared)
Opens and reads the 06.01 Radius.txt file
Calculates and prints the radius, diameter, circumference, and area on a line. (each value is 15 columns wide, 5 decimal digits, and a space seperating each column.
Print headings that right align with the data.
"""
import math

print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius", "Diameter", "Circumference", "Area"))
def diameter(radius):
    return 2 * radius

def circumference(radius):
    return 2 * math.pi * radius

def area(radius):
    return math.pi * radius ** 2

# Open and read the Radius.txt file
file = open("06./06.01 Radius.txt")
for num in file:
    radius = float(num)
    print("{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}".format(radius, diameter(radius), circumference(radius), area(radius)))
