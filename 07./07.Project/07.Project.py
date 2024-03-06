# Open files and set appropriate read vs write variables
input_file = open("07./07.Project/07.Project Angles Input.txt", "r")     
output_file = open("07./07.Project/07.Project Angles Output.txt", "w")
#set initial variables
records = 0

def ParseDegreeString(string):
    degrees = string[1:2]
    minutes = string[3:4]
    seconds = string[5:6]
    return (degrees, minutes, seconds)

def DDMMStoDecimal(degrees,minutes,seconds):
    decimal_degrees = degrees + (minutes/60) + (seconds/3600)
    return (decimal_degrees)


for line in input_file:
    ParseDegreeString(line)
    degrees = ParseDegreeString(degrees)
    minutes = ParseDegreeString(minutes)
    seconds = ParseDegreeString(seconds)
    decimal_degrees = DDMMStoDecimal(degrees, minutes, seconds)
    output_file.write(decimal_degrees)
    records += 1

"""def circumference(radius):
    return 2 * math.pi * radius

def area(radius):
    return math.pi * radius ** 2

# Open and read the Radius.txt file
file = open("06./06.01 Radius.txt")
for num in file:
    radius = float(num)
    print("{:>15.5f} {:>15.5f} {:>15.5f} {:>15.5f}".format(radius, diameter(radius), circumference(radius), area(radius)))"""


# Close both files
input_file.close()
output_file.close()
print(records, "records processed")




