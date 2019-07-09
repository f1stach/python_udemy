import random

my_number = random.randint(0,20)

guess = -1
trials = 0

print("Guess my number!")

while guess != my_number:
    guess = int(input())
    trials = trials + 1

    if guess > my_number:
        print("Sorry- my number is smaller than your guess, Try again!")
    elif guess < my_number:
        print("Sorry- my number is greater than your guess, Try again!")
    else:
        print("You won! The number is", guess)
        print("It took", trials, "trials to guess!")

