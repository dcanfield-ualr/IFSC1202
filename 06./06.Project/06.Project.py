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
# Open and read from the input file
input_file = open("06./06.Project/06.Project Input File.txt", "r")     
output_file = open("06./06.Project/06.Project Output File.txt", "w")
input_records = 0
merge_records = 0
output_records = 0

line = input_file.readline()

while line != "**Insert Merge File Here**":
     output_file.write(line)
     input_records += 1
     output_records += 1
     if line == "**Insert Merge File Here**":
     # Open and read from the merge file
          merge_file = open("06./06.Project/06.Project Merge File.txt", "r")
          for merge_line in merge_file:
               output_file.write(merge_line)
               merge_records += 1
               output_records += 1
               merge_file.close()
               # Continue copying lines from input file after merge
               for remaining_line in input_file:
                    output_file.write(remaining_line)
                    input_records += 1
                    output_records += 1
                    break  # Stop reading input file after merge
                
# Close both files
input_file.close()
merge_file.close()
output_file.close()
print("Number of input records:", input_records)
print("Number of merge records:", merge_records)
print("Number of output records:", output_records)