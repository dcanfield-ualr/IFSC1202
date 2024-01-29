#Given a month - an integer from 1 (January) to 12 (December),
#print the number of days in the month.
#Assume that it is a non-leap year.

num = int(input("Enter Month: "))

#28 days February(02)
#30 days April(04), June(06), September(09), November(11)
#31 days January(01), March(03), May(05), July(07), August(08), October(10), December(12)

if num == 2:
    print("28 days")
elif num == 4 or num == 6 or num == 9 or num == 11:
    print("30 days")
else:
    print("31 days")