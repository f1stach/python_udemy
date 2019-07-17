import random

# przechowujemy wylosowane numery:
myNumbers = []

# losowanie tak dlugo az osiagniemy 7 numerow:
while len(myNumbers) < 7:
    newNumber = random.randint(1,49)

    # sprawdzamy czy nie ma duplikatu. Instrukcja continue powoduje przeskok do początku while:
    if newNumber in myNumbers:
        print("Eliminated:", newNumber)
        continue

    myNumbers.append(newNumber)

print("Those are winning numbers:", myNumbers)


# ZADANIA
print("--------------------------")
print("ZAD. 1 - KARTY")

import random

colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
figures = ["Ace", "King", "Queen", "Jack", "10", "9"]
allCards = []
player1 = []
player2 = []

# join colors and figures:
for i in colors:
    for j in figures:
        joined = i + " " + j
        allCards.append(joined)
print("Joined cards:", allCards)

# shuffle joined cards:
random.shuffle(allCards)
print("Shuffled cards:", allCards)


# give cards to players -1st way - one card goes to player1 and one goes to player2
maxx = len(allCards)

# i = 0
for i in range(maxx):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
    # i += 1

print("\nFirst option:")
print("Player's 1 cards:", player1)
print("Player's 2 cards:", player2)
#

# give cards to players - 2nd way - 12 cards go to player1 and 12 goes to player2

player1 = allCards[:11]
player2 = allCards[12:23]

print("\nSecond option:")
print("Player's 1 cards:", player1)
print("Player's 2 cards:", player2)
