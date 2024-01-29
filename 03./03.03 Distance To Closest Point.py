#Given the coordinates of the three points A, B, and C on a line.
#print a distance from the point A to closest point to it.
#Hint: Determine the distance from A to B by subtracting B from A, 
#then determine the distance from A to C by subtracting C from A. 
#Determine the smallest distance.

num1 = int(input("Enter Point A: "))
num2 = int(input("Enter Point B: "))
num3 = int(input("Enter Point C: "))
#ensure to use absolute value abs() 
dist1 = abs(num1 - num2)
dist2 = abs(num1 - num3)
           
if dist1 < dist2:
    print(dist1)
else:
    print(dist2)