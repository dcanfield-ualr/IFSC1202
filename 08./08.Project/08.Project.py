import requests

# Read the US Constitution from the internet
url = "https://www.usconstitution.net/const.txt"
response = requests.get(url)
constitution_text = response.text

# Split the text into a list of strings, each line being an item in the list
constitution_lines = constitution_text.split('\n')

# Prompt for a search term
while True:
    search_term = input("Enter a search term (press Enter to exit): ").strip()
    if not search_term:
        break
    found = False

# Search for the search term in each line
    for i, line in enumerate(constitution_lines):
        if search_term.lower() in line.lower():
            found = True
            print("Search term found in line", i,":")
                
# Loop backwards to find the beginning of the section
            start_line = i
            while start_line >= 0 and constitution_lines[start_line].strip() != "":
                start_line -= 1

# Loop forwards to find the end of the section
            end_line = i
            while end_line < len(constitution_lines) and constitution_lines[end_line].strip() != "":
                end_line += 1

# Print the section of text that contains the search term along with the line number
            for j in range(start_line, end_line+1):
                print(f"Line {j}: {constitution_lines[j]}")
                
# Skip to the end of the section
            i = end_line

    if not found:
        print("Search term not found.")