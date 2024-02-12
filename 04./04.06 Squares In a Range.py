#Given two integers A and B, print squares of all integer numbers between them inclusively as shown below.
#Be sure to print the formula as shown.
#There are no spaces around * and =.
#You can use either the sep= argument of the print() statement or the .format method.

# Read the integer Num
numA = int(input("Enter A: "))
numB = int(input("Enter B: "))

#numA = current iteration starting at 0
#numA+=numA for each loop
#for loop stops numB-1 ensure to +1
for numA in range(numB+1): 
    print(numA, numB)
    print(numA,"*",numA,"=",numA*numA)
