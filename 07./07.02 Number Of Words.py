"""Prompt for a string consisting of words separated by a single space. Display how many words it has."""
string = str(input("Enter a string: "))
num = 1
num += string.count(" ")
print(num,"words")