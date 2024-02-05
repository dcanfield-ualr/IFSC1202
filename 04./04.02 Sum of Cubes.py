#For the given integer N, calculate the sum cubes of each number from 1 to N.
#1**3 + 2**3 + … + N**3

num = int(input("Enter Number: "))
result = 0

for i in range(num):
    result += (i+1)**3
   
print(result)