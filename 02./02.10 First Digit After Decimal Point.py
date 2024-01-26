#create variable num1 and assign value as integer input including prompt
num = float(input("Enter a Number: "))
#subtract int cast of num from num to provide fraction.
num = num - int(num)
#multiply decimal by 10 to change decimal place.
num = num * 10
#print while using casting num as int to remove fractional remainder
print("Tenths Value: ", int(num))