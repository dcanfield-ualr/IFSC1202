"""
Create a program that displays a list or prime number in a specified range.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Hint: For a given value N, Loop from 2 to (half of N) + 1 and check to see if any number evenly divides into N.
"""
start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

print("Prime numbers between",start,"and",end)

for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2,(num**0.5) + 1):
            if num % i == 0:
                prime = False
        if prime:
            print(num)
