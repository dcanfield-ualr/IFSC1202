#Prompt for three integers and print them in ascending order.
    
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

# Arrange the numbers in ascending order
sorted_numbers = sorted([num1, num2, num3])

# Print the sorted numbers
print(sorted_numbers[0], sorted_numbers[1], sorted_numbers[2])

# Arrange the numbers in ascending order using if statements
if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle = num1
        largest = num3
    else:
        middle = num3
        largest = num1
else:
    smallest = num3
    if num1 <= num2:
        middle = num1
        largest = num2
    else:
        middle = num2
        largest = num1

# Print the sorted numbers
print("The numbers in ascending order are:", smallest, middle, largest)


