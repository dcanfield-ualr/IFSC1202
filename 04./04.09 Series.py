#Prompt for two integer values A and B.
#If A < B, print all numbers from A to B inclusively in ascending order.
#If A ≥ B, print all numbers from B to A inclusively in descending order.
A = int(input("Enter A: "))
B = int(input("Enter B: "))

if A < B:
    for i in range(A,B+1):
        print(i)
    print()
if A > B:
    for i in range(B,A+1):
        print(i)
    print()
