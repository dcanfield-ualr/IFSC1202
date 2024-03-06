# Open files and set appropriate read vs write variables
input_file = open("07./07.Project/07.Project Angles Input.txt", "r")     
output_file = open("07./07.Project/07.Project Angles Output.txt", "w")
#set initial variables
records = 0

def parseDegreeString(ddmmss):
    degree_idx = ddmmss.find(chr(176))
    minute_idx = ddmmss.find("'")
    second_idx = ddmmss.find('"')

    degrees = float(ddmmss[:degree_idx])
    minutes = float(ddmmss[degree_idx + 1:minute_idx])
    seconds = float(ddmmss[minute_idx + 1:second_idx])
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimal_degrees = degrees + (minutes/60) + (seconds/3600)
    return decimal_degrees
    
for line in input_file:
    degrees, minutes, seconds = parseDegreeString(line)
    decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
    output_file.write(str(decimal_degrees))
    output_file.write("\n")
    records += 1

# Close both files
input_file.close()
output_file.close()
print(records, "records processed")