#Prompt for a 4 digit year
#If the year is a leap year, print "LEAP YEAR", otherwise print "COMMON YEAR".
#The rules in Gregorian calendar are as follows:
#a leap year is exactly divisible by 4 is not exactly divisible by 100
#a leap year is exactly divisible by 400

year = int(input("Enter Year: "))

#if the remainder of year/4 = 0 and remainder of year/100 doesnt = 0 
#if the remainder of year/400 = 0
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("LEAP YEAR")
else:
    print("COMMON YEAR")

