import csv

# Function to read the distances between cities from the CSV file
def read_distance_table(file_path):
    distances = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            distances.append(row)
    return distances

# Function to print the distance table
def print_distance_table(table):
    for row in table:
        print(row)

# Function to find the index of a city in the distance table
def find_city_index(city, cities_list):
    try:
        index = cities_list.index(city)
        return index
    except ValueError:
        return None

# Main function
def main():
    file_path = "09.Project Distances.csv"
    distance_table = read_distance_table(file_path)
    
    # Print the distance table
    print("Distance Table:")
    print_distance_table(distance_table)
    
    # Prompt for From City
    from_city = input("Enter From City: ")
    from_index = find_city_index(from_city, [row[0] for row in distance_table])
    if from_index is None:
        print("Invalid From City")
        return
    
    # Prompt for To City
    to_city = input("Enter To City: ")
    to_index = find_city_index(to_city, distance_table[0])
    if to_index is None:
        print("Invalid To City")
        return
    
    # If both cities were found, display the distance
    distance = distance_table[from_index][to_index]
    print(f"Distance from {from_city} to {to_city}: {distance}")

if __name__ == "__main__":
    main()
