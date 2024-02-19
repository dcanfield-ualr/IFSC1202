"""
Prompt for a sequence of numbers, the last number being carriage return
Print the average of the numbers
If no data is entered (only a carriage was entered), you will generate an error (division by zero). If no data is entered, print "Sequence Length is 0".
"""

num = 0
sum = 0
total = 0
while num != "": 
    num = int(input("Enter a Number (CR to quit): "))
    
    sum = sum + num
    total = total + 1

else:
    print("Sum: ",sum/total)