from random import randint
name = input("Hello! What is your name? ")
print("Well,",name,", I am thinking of anumber between 1 and 20")
print("You have 5 guesses")
num = randint(1,20)
#had to define i, in FOR loops decleration is in statement
i = 0
#started with for loop wanted to try with while loop
for i in range(5):
#while i < 5:
    guess = int(input("Take a guess: "))
    if guess > num:
        print("Your guess is too high.")
    if guess < num:
        print("Your guess is too low.")
    if guess == num:
        print("Good job, Joe! You guessed my number in",i,"guesses!")
        break
    if i == 4:
        print("Nope. The number is was thinking of was", num)
#else:
        #print("Nope. The number is was thinking of was", num)

     