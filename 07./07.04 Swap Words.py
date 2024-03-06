"""
Prompt for a string consisting of exactly two words separated by a space.
Print a new string with the first and second word positions swapped (the second word is printed first).
This task should not use loops or an if statement.
"""

string = str(input("Enter a string: "))
space_index = string.find(" ")

half1 = string[:space_index]
half2 = string[space_index:]

print(half2,half1)