"""
Prompt for a string. Determine if the string contains the letter "f"
If the string contains one letter "f", print the index
If the string contains more than one letter "f", print the index of the first and last occurance
If the string does not contain any letter "f", then do not print zero (0)
"""

string = "office" #str(input("Enter a string: "))
space_index = string.find("f")
space_indexR = string.rfind("f")

if space_indexR != 0:
    print(space_index)

elif space_index != 0:
    print(space_index,space_indexR)
else:
    print("not zero")   