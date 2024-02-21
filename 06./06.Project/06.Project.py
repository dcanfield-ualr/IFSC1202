"""
Create a python solution that merges the contents of two files into a new file.
Open 06.Project Output File.txt for writing
Open and read 06.Project Input File.txt, copying lines from 06.Project Input File.txt to 06.Project Output File.txt line by line. Keep a count of the number of input records and output records.
Inspect each line of the input file for the text: **Insert Merge File Here**
At this point, open 06.Project Merge File.txt, copying lines from 06.Project Merge File.txt to 06.Project Output File.txt line by line. Keep a count of the number of merge records and output records.
At the end of 06.Project Merge File.txt, continue copying lines from 06.Project Input File.txt to 06.Project Output File.txt line by line. Keep a count of the number of input records and output records.
Close all files
Print the number of records in the input file, merge file, and output file.
"""

# The name of the file can be a string
#inputfilename = "06./06.Project/06.Project Input File.txt"
#mergefilename = "06./06.Project/06.Project Merge File.txt"
#outputfilename = "06./06.Project/06.Project Output File.txt"
recordcount = 0
# Open the input file for reading
inputfile = open("06./06.Project/06.Project Input File.txt", 'r')
# Open the merge file for reading
mergefile = open("06./06.Project/06.Project Merge File.txt", 'r')
# Open the output file for writing
outputfile = open("06./06.Project/06.Project Output File.txt", 'w')
# Read the first line of the input file

#debug
# Read the entire contents of the file into a single string
i = inputfile.read()
# Print the contents - Note the embedded linefeeds
print(i)
# Close the file
inputfile.close()

# Read the entire contents of the file into a single string
m = mergefile.read()
# Print the contents - Note the embedded linefeeds
print(m)
# Close the file
mergefile.close()
# Read the entire contents of the file into a single string
o = outputfile.read()
# Print the contents - Note the embedded linefeeds
print(o)
# Close the file
outputfile.close()




print(inputfile)
line = inputfile.readline()
# Read until the input is empty
while line != "**Insert Merge File Here**":
# Write to the output file
# Note that line already contains a linefeed character,
# so we don't have to add one when we write it.
     outputfile.write(line)
     recordcount += 1
# Read the next line of the input file
     line = inputfile.readline()
if line == "**Insert Merge File Here**":
     merge = mergefile.readline()
     while merge != "":
        outputfile.write(line)
        recordcount += 1
        break
#else:
     #while line != "" or "**Insert Merge File Here**":
# Write to the output file
# Note that line already contains a linefeed character,
# so we don't have to add one when we write it.
          #outputfile.write(line)
          #recordcount += 1
# End of File on input file
# Close both files
inputfile.close()
mergefile.close()
outputfile.close()
print("{} records written".format(recordcount))