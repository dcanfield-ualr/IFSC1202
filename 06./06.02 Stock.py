"""
You have a file that has the stock prices for a week, one per line.
Create a program that performs the following:
Defines a function called "percentchange"
Accepts today stock price (floating point) and yesterdays stock price (floating point) as parameters
Calculates and percent change between yesterdays and todays stockprice
Percent Change is todays stock value - yesterdays stock value divided by yesterdays stock value time 100
Opens and reads the first line of 06.02 Stock.txt file
Prints headings and the first stock value (there is no percent change on the first day)
Reads the next line of input
Calculates and prints the stock value and the percent change from yesterday. Each column is 10 characters wide with a space between them.
"""

def percentchange(Yprice,Tprice):
    return (Yprice-Tprice)/Yprice
#create "header"
print("{:^10s}{:^10s}".format("Price","Change"))
# Open and read the Stock.txt file
stock_file = open("06./06.02 Stock.txt")
Tprice = 1
Yprice = 1
for num in stock_file:
    Yprice = Tprice
    Tprice = float(num)
    print("{:^10}{:^10}".format(Tprice, percentchange(Yprice,Tprice)))
