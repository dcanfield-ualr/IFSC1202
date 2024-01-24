days = int(input("Enter Length of Time in Days: "))
#use floor division to return whole number of years
years = int(days//365)
print("Years: "+str(years))
#subtract years from days
days -= years*365
#use floor division to return whole number of weeks
weeks = int(days//7)
print("Weeks: "+str(weeks))
days -= weeks*7
print("Days: "+str(days))