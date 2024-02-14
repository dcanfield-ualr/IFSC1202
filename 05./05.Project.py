"""
Create a program that displays special numbers in a range. A special number is defined to be number that is the sum of its own digits each raised to the power of the number of digits.
153 is 3 digits long and is equal to 13 + 53 + 33
8208 is 4 digits long and is equal to 84 + 24 + 04 + 84
Hint: First determine the number of digits using a while loop and reminder division by 10. Do not use any string functions or the LEN function.
Hint: Recalculate the value using the power from above and see if you get the original value
Do not use the len function to determine the number of digits.
"""

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Special numbers between",start,"and",end)

for num in range(start, end + 1):
    total = 0
    num_digits = 0
    
    # Calculate the number of digits
    temp = num
    while temp != 0:
        temp //= 10
        num_digits += 1
    
    # Calculate the sum of digits raised to the power of the number of digits
    temp = num
    while temp != 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    #validate and print special number
    if total == num:
        print(num)
