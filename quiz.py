import  random

ran = random

guess = ran.randint(1, 30)
print("Guess number from 1- 30")
print(guess)
life = 3
print("life:", life)
while True:

    userInput = int(input("enter number"))

    if userInput > guess:

        print("Lower")
        life -=1
        print("You have only ", life, "left")
    elif userInput < guess:
        print("Higher")
        life-=1
        print("You have only ", life, "left")

    elif userInput == guess:
        print("Good Job")
        break

    if life == 0:
        print("You Loss")
        print("You have only ", life, "left")
        break