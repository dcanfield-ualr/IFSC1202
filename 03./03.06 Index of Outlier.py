#Prompt for three integers: two are equal to each other and the third one is different.
#Print the index number of the different one, either 1, 2 or 3.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
           
if num1 != num2 and num1 != num3:
    print("1")
elif num2 != num1 and num2 != num3:
    print("2")
else:
    print("3")