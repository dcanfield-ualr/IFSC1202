#Given an integer N, print the sum of: 1! + 2! + 3! + ... + N!
#This problem has a solution with only one loop, so try to discover it.
#Don't use the math library.

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


