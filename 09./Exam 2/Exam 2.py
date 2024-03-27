"""
Exam Two Properties.csv contains the following real estate property information seperated by a comma:
Column 0 - Address
Column 1 - City
Column 2 - State
Column 3 - Zip Code
Column 4 - Price
Open Exam Two Properties.csv and read a line from the file.
The data for each property is separated by a comma. Split each line of data into a one dimensional list.
Convert the price to a floating point number
Append the one dimensional list to a two dimensional list called "properties" that contains all of the data in Exam Two Properties.csv (40 points).
Create an empty two dimensional list called "zipcodes". Each row in list will contain:
Column 0 - Zip Code
Column 1 - Count of the number or properties with this zip code
Column 2 - Sum of the price of the propeties in this zip code
Loop though all of the rows in the "properties" list (10 points)
Loop through the rows in the "zipcodes" list (10 points)
When there is a match between the zip code in the properties list (Column 3) and the zipcode in the zipcode list (Column 0) then
Increment the number of properties found for that zip code (Column 1 in the zipcode list) (20 points)
Add the price of the property (Column 4 in the property list) to the sum of the prices (Column 2 in the zipcode list) (20 points)
If no match is found
Append a row to "Zipcodes", where Column 0 is the zipcode, Column 1 is the initial count (1), and Column 2 is the price of the property (20 points)
Print the headings of the report
Loop through all of the values in "zipcodes" and print (30 points):
Zipcode (Column 0)
Count of Properties (Column 1)
Average Property Price - calculated as Sum of Prices (Column 2) divided by the Count of Properties (Column 1)
"""

# Open Exam Two Properties.csv and read a line from the file
file = open('09./Exam 2/Exam Two Properties.csv', 'r')
# Initialize a two dimensional list called "properties" to store property data
properties = []

# Split each line of data into a one dimensional list and append to properties list
for line in file:
    data = line.strip().split(',')
 # Convert price to floating point number   
    data[4] = float(data[4])  
    properties.append(data)

# Initialize a two dimensional list called "zipcodes" to store zipcode data
zipcodes = []

# Loop through all rows in the properties list
for prop_data in properties:
    zip_code = prop_data[3]
    found = False
# Loop through rows in the zipcodes list
    for zip_data in zipcodes:
        if zip_data[0] == zip_code:
# Increment the count of properties and add price to sum
            zip_data[1] += 1
            zip_data[2] += prop_data[4]
            found = True
            break
    if not found:
# If no match found, append a new row to zipcodes where column0=zipcode, column1=1, column2=price 
        zipcodes.append([zip_code, 1, prop_data[4]])

# Print headings of the report
print("    Zipcode   Count      Average")

# Loop through zipcodes list and print data
for zip_data in zipcodes:
    zip_code = zip_data[0]
    count = zip_data[1]
    total_price = zip_data[2]
    average_price = total_price / count
    print(f"     {zip_code : >1}      {count : >2}    ${average_price:>5,.2f}")
