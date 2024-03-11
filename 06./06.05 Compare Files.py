"""
You have a two files. You want to compare them line by line and print the differences.
Create a program that performs the following:
Opens the file 06.05 CompareFileA.txt file for reading
Opens the file 06.05 CompareFileB.txt file for reading
Read a line from both files
If the line from both files is not the same, print the line number and the contents of both lines
Print the number of differences
"""
# Open files and set appropriate read vs write variables
FileA = open("06./06.05 CompareFileA.txt", "r")   
FileB = open("06./06.05 CompareFileB.txt", "r") 

#set initial variables
input_records = 0
merge_records = 0
output_records = 0

#iterate "read loop"
for line in FileA:
     #check if line is insertion prompt ensure newline is included
     if line == "**Insert Merge File Here**\n":
          #open file and set read variable
          merge_file = open("06./06.Project/06.Project Merge File.txt", "r")
          #iterate "read loop"
          for merge_line in merge_file:
               #write input(merge) to output file and append records
               output_file.write(merge_line)
               merge_records += 1
               output_records += 1
          #remember to add newline if not included from input
          output_file.write("\n")
          merge_file.close()
     else:
          #write input(input) to output file and append records            
          output_file.write(line)
          input_records += 1
          output_records += 1
# Close both files
FileA.close()
FileB.close()
print("Number of input records:", input_records)
print("Number of merge records:", merge_records)
print("Number of output records:", output_records)