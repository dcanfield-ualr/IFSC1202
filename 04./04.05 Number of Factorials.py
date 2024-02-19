#Given an integer N, print the sum of: 1! + 2! + 3! + ... + N!
#This problem has a solution with only one loop, so try to discover it.
#Don't use the math library.

# Read the integer N
N = int(input("Enter N: "))
#ensure num starts at one, values are multiplied
num = 1
#ensure sum starts at zero, values are added
sum = 0

#i = current iteration starting at 0
#i+=i for each loop
for i in range(N): 
    #ensure i+1 to prevent A*0=0
    num *= (i+1)
    #add to sum
    sum += num
print("Sum of Factorials: ",sum)