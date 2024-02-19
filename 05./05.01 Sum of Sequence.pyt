"""
Prompt for a sequence of numbers, the last number being a carriage return.
Print the sum of the numbers.
"""
sum = 0
num = input("Enter a Number (CR to quit): ")
while num != "": 
      sum = sum + int(num)
      num = input("Enter a Number (CR to quit): ")
print("Sum: ",sum)
