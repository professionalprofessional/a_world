import random 

dice_roll = random.randint(1,100)

guess = int(input("Guess a number between 1 to 100 "))
count = 1
while guess !=dice_roll:
    count = count + 1
    if dice_roll <= guess:
        print("Your Guess Is Too High")
    else:
        print("Your Guess Is Too Low")

    guess = int(input("Nice Try, Guess Again 1 to 100"))

print("Awsome!!! It Took you", count, "times!!" )


