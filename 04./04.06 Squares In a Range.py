#Given two integers A and B, print squares of all integer numbers between them inclusively as shown below.
#Be sure to print the formula as shown.
#There are no spaces around * and =.
#You can use either the sep= argument of the print() statement or the .format method.

# Read the integer N
N = int(input("Enter N: "))
num = 1
sum = 0

for i in range(1, N+1): 
    num *= i
    print(num)
    sum += num
    print(sum)
print("Sum of Factorials: ",sum)