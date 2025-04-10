# Create a basic number guessing game.
import random

num = random.choice([1, 2, 3, 4, 5, 6,7,8,9,10])
while True:
    user_num = int(input("Enter a number between 1 to 10: "))
    if user_num <= 10:
        if num == user_num:
            print("you win")
            break
        else:
            print("you lose")
            break
    else:
        print("I said between 1 and 10!")