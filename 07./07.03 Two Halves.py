"""
Prompt for a string and cut it into two "equal" parts (If the length of the string is odd, place the center character in the first string, so that the first string contains one more characther than the second).
Print a new string on a single row with the first and second halves interchanged (second half first and the first half second)
Don't use the if statement in this task.
"""

string = str(input("Enter a string: "))
string_length = int(len(string)/2)

half1 = string[:string_length]
half2 = string[string_length:]

print(half2+half1)