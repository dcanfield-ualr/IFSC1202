#Prompt for a month (an integer from 1 to 12) and a day in the month (an integer from 1 to 31) in a common year (not a leap year).
#Print the month and the day of the next day after it.

month = int(input("Enter Month:"))
day = int(input("Enter Day: "))
    
print("Next Day: ", month,"/",day)

# Determine the number of days in the given month
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Check if it's the last day of the month
if day == days_in_month[month]:
     # If yes, advance to the next month and set the day to 1
    month += 1
    day = 1
    # Check if it's the next year
    if month == 13:
        month = 1
else:
    # If not, simply increment the day
    day += 1

# Print the result
print("The next day is: {} {}".format(month, day))