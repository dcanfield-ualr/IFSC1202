#N numbers are given in the input. Read them and print their product.
#The first line of input contains the integer N, which is the number of integers to follow.
#Each of the next N lines contains one integer. Print the product of these N integers.

n = int(input("Enter N: "))
result = 1

for i in range(n):
    num = int(input("Enter Number: "))
    # result = result + i
    result = result * num  
print(result)