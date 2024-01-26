#create variable num1 and assign value as integer input including prompt
num1 = int(input("Enter First 2 Digit Number: "))
#remainder after division of 10 
num1one = num1 % 10
#floor division by ten provides value of ten
num1ten = num1 // 10
#create variable num2 and assign value as integer input including prompt
num2 = int(input("Enter First 2 Digit Number: "))
#remainder after division 0f 10
num2one = num2 % 10
#floor division by ten provides value of ten
num2ten = num2 // 10
print("{}{}{}{}".format(num1ten,num2ten,num1one,num2one))

