#create variable num and assign value as integer input including prompt
num = int(input("Enter a number: "))
#create variable one and assign value of remainder of input /10 
one = num % 10
#create variable ten and assign value of input after floor division
ten = num // 10
#print values with a blank format "template"
print("Ones Digit:","{}".format(one))
print("Tens Digit:","{}".format(ten))