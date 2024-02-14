"""
Create a program that displays a list or prime number in a specified range.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Hint: For a given value N, Loop from 2 to (half of N) + 1 and check to see if any number evenly divides into N.
"""
start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
#creates title for following data set
print("Prime numbers between",start,"and",end)
#runs loop within user defined range (remember for stops before max value)
for num in range(start, end + 1):
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
            print(num)
