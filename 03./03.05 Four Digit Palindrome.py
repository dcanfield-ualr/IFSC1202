#Given a four-digit integer, print "YES" if it's a palindrome
#print "NO" otherwise.
#Hint: put the units, tens, hundreds, and thousands in separate variables. 
#Do not use any string functions.

num = int(input("Enter a Number: "))
#create variable one and assign value of remainder of input /10 
one = num % 10
#create variable ten and assign value of input after floor division
ten = (num//10) % 10
#create variable hundred and assign value of input after floor division
hundred = (num//100) % 10
#create variable thousand and assign value of input after floor division
thousand = num // 1000

if one == thousand and ten == hundred:
    print("YES")
else:
    print("NO")