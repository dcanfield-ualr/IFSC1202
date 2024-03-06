# Open files and set appropriate read vs write variables
input_file = open("07./07.Project/07.Project Angles Input.txt", "r")     
output_file = open("07./07.Project/07.Project Angles Output.txt", "w")
#set initial variables
records = 0
"""
def ParseDegreeString(line):
    degrees = line[1:2]
    minutes = line[3:4]
    seconds = line[5:6]
    return (degrees, minutes, seconds)

def DDMMStoDecimal(degrees,minutes,seconds):
    decimal_degrees = (degrees) + (minutes/60) + (seconds/3600)
    return (decimal_degrees)


for line in input_file:
    ParseDegreeString(line)
    degrees = int(ParseDegreeString(degrees))
    minutes = ParseDegreeString(minutes)
    seconds = ParseDegreeString(seconds)
    decimal_degrees = DDMMStoDecimal(degrees, minutes, seconds)
    output_file.write(DDMMStoDecimal(decimal_degrees))
    records += 1
"""


for line in input_file:
    degrees = int(line[1:2])
    minutes = int(line[3:4])
    seconds = int(line[5:6])
    decimal_degrees = (degrees) + (minutes/60) + (seconds/3600)
    output_file.write(decimal_degrees)
    records += 1

# Close both files
input_file.close()
output_file.close()
print(records, "records processed")




