#For given integer N ≤ 9, print a ladder of N steps.
#The Kth step consists of the integers from 1 to K without spaces between them.
#You can use the sep= and end= arguments of the print() function.
#Hint: You can use a For loop within a For loop.

# Read the integer N
N = int(input("Enter N: "))

#i = current iteration starting at 0
#i+=i for each loop
#for loop stops N-1 ensure to +1\
for i in range(1,N+1):
     for k in range(1,i+1):
        print(k, sep='', end='')
     print()   