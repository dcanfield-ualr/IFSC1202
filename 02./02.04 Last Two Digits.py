#create variable num and assign value as integer input including prompt
num = int(input("Enter a number: "))
#create variable one and assign value of remainder of input /10 
one = num % 10
#create variable ten and assign value of input after floor division
ten = num // 10
#print & swap values 
print(ten,one)

print("{:0004d}".format(4258))           #|0|0|3|.|1|4|