import random 

dice_roll = random.randint(1,100)

guess = int(input("guess a number "))
while guess !=dice_roll:
    guess = int(input("guess another number"))
count = 1



print("Awesome! You got it!!")

#if guess==dice_roll:
#    print("correct!")
#else:
 #   print("bad guess, the correct number was:", dice_roll) 

