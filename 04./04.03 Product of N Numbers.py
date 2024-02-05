#In mathematics, the factorial of an integer N, denoted by N! is the following product:
#N! = 1 × 2 × … × N
#For the given integer N, calculate the value N!
#Don't use math module in this exercise.

num = int(input("Enter Number: "))
result = 1

for i in range(num):
    result *=  (i+1)   
print(result)