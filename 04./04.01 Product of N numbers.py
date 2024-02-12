#N numbers are given in the input. Read them and print their product.
#The first line of input contains the integer N, which is the number of integers to follow.
#Each of the next N lines contains one integer. Print the product of these N integers.

#Create n which represents number of iterations
n = int(input("Enter N: "))
#Create result as 1. 0*a=0
result = 1

#i = current iteration starting at 0
#i+=i for each loop
 
for i in range(n):
    num = int(input("Enter Number: "))
    result = result * num  
print(result)