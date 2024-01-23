days = int(input("Enter Length of Time in Days: "))
years = int(days//365)
print("Years: "+str(years))
days -= years*365
weeks = int(days//7)
print("Weeks: "+str(weeks))
days -= weeks*7
print("Days: "+str(days))