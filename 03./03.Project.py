"""
Create a simple calculator program and prompts for 2 operands and an operator, then calculates the result.
Prompt for the first operand (either integer or floating point)
Prompt for a operator, where:
+ addtion
- subtraction
* multiplication
\ division
If an invalid operator is entered, then display "Invalid Operator" (Do not display an invalid calculation)
If a valid operator is entered, display the first number, the operand, the second number, an equals sign, and the result of the calculation
"""

num1 = float(input("Enter First Number: "))
operator = input("Enter Operator (+,-,*,/): ")
num2 = float(input("Enter Second Number: "))

print(num1, operator, num2, "=", (num1+num2))