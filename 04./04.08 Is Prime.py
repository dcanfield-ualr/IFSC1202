#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#Given an integer N > 1, print PRIME if it's prime and print COMPOSITE otherwise.
#Hint: Loop from 2 to (half of N) + 1 and check to see if any number evenly divides into N.

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