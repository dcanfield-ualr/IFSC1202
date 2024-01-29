#Given three integers, determine how many of them are equal to each other.
#The program must print one of these numbers:
#3 (if all are the same),
#2 (if two of them are equal to each other and the third is different) or
#0 (if all numbers are different).

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
           
if num1 == num2 == num3:
    print("3")
# != not equal
elif num1 != num2 and num1 != num3:
    print("0")
else:
    print("2")