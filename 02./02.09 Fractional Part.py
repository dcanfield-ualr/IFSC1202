#create variable num1 and assign value as integer input including prompt
num = float(input("Enter a Number: "))
#subtract int cast of num from num to provide fraction.
num = num - int(num)
#print while using round function to specify limit of 10 characters
print("Fractional Part: ", round(num,10))