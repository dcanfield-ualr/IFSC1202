#create variable num and assign value as integer input including prompt
num = int(input("Enter a 3 digit number: "))
#create variable one and assign value of remainder of input /10 
one = num % 10
#create variable ten and assign value of input after floor division
ten = (num//10) % 10
#create variable ten and assign value of input after floor division
hundred = num // 100
#print values with correct format
print("Reverse of Digits:","{}{}{}".format(one,ten,hundred))

