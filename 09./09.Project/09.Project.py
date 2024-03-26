"""
Create a python solution that reads a table containing the distansces between cities. Prompt for a From City and a To City, search the table, and print the distance between the cities.
Logic
The input file, 09.Project Distances.csv, is a conmma separated value file, with the From City in the zeroth colunmn and the To City in the zeroth row.
Read the input file and load each line into a row of a two dimensional list.
Print the two dimensional list
Prompt for a From City
Prompt for a To City
Search the zeroth column for the From City. Save the index of the row where the city was found.
Search the zeroth row for the To City. Save the index of the column where the city was found.
If the From City was not found, then display "Invalid From City".
If the To City was not found, then display "Invalid To City".
If both cities where found, display the From City, To City, and the Distance.
"""
# Read the distances between cities from the CSV file
distances = []
file = open("09./09.Project/09.Project Distances.csv", 'r')
for line in file:
    distances.append(line.strip().split(','))

# Print the distance table with right-aligned columns
for row in distances:
    row_str = ""
    for cell in row:
        row_str += cell.rjust(10)  # Adjust the width as needed
    print(row_str)
    
# Prompt for From City
from_city = input("Enter From City: ")
from_index = None
for i, city in enumerate(distances):
    if city[0] == from_city:
        from_index = i
        break
#Error Message
if from_index is None:
    print("Invalid From City")
else:
# Prompt for To City
    to_city = input("Enter To City: ")
    to_index = None
    for i, city in enumerate(distances[0]):
        if city == to_city:
            to_index = i
            break
#Error Message
    if to_index is None:
        print("Invalid To City")
    else:
        distance = distances[from_index][to_index]
        print(f"Distance from {from_city} to {to_city}: {distance}")