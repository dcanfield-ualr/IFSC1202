side1 = float(input("Enter Side 1:"))
side2 = float(input("Enter Side 2:"))
side3 = float(input("Enter Side 3:"))
#s represents half the perimeter, used for calculating area
s = float((side1+side2+side3)/2)
#calculate area using Herons formula, sqrt = **0.5
area = (s*((s-side1)*(s-side2)*(s-side3)))**0.5

print(area)