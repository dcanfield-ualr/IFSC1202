#Given N numbers: the first number in the input is N, after that N integers are given.
#Count the number of zeros among the given integers and print it.
#You need to count the numbers that are equal to zero, not the number of zero digits.

N = int(input("Enter N: "))
#create zero variable as "counter" of zeros
zero = 0

#i = current iteration starting at 0
#i+=i for each loop
for i in range(N): 
    #create num variable to pass user input to validation
    num = int(input("Enter Number: "))
    #if user input is 0 add to counter
    if num == 0:
        zero += 1
print("Number of Zeros:",zero)