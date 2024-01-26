#create variable num and assign value as integer input including prompt.
num = int(input("Enter a number: "))
#floor division to remove ones place
num = num // 10
#remainder after 10 isolates tens place
num = num % 10
#print and format specifying leading zeroes, 1 characters, d for integer
print("Tens Digit:","{:01d}".format(num))