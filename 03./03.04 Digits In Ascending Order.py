#Given a three-digit integer
#print "YES" if its digits are in ascending order left to right
#print "NO" otherwise.
#Do not try to sort the number. 
#Determine each digit and use "if" statements.
num = int(input("Enter a Number: "))
#create variable one and assign value of remainder of input /10 
one = num % 10
#create variable ten and assign value of input after floor division
ten = (num//10) % 10
#create variable ten and assign value of input after floor division
hundred = num // 100
           
if hundred < ten < one:
    print("YES")
else:
    print("NO")