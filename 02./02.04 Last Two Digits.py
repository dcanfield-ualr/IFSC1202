#create variable num and assign value as integer input including prompt
num = int(input("Enter a number: "))
#remainder after 100 isolates last two places
num = num % 100 
#print and format specifying leading zeroes, 2 characters, d for integer
print("Last Two Digits:","{:02d}".format(num))