# W definicji karty mamy teraz 2 informacje. Figurę karty - tutaj "King" i jej moc - tutaj 12
# aCard = {"Figure":"King", "Power":12}
# print(aCard)
# print(aCard['Figure'])
# print(aCard['Power'])
# aCard['Color'] = 'Heart'
# print(aCard['Color'])
# print(aCard)

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

player1 = []
player2 = []

# join colors and figures:
for i in colors:
    for j in figures:
        aCard = j.copy()
        aCard["Color"] = i
        allCards.append(aCard)

import random

maxx = len(allCards)

random.shuffle(allCards)
print("Shuffled cards:", allCards)

# give cards to players:
for i in range(maxx):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

print("Player's 1 cards:", player1)
print("Player's 2 cards:", player2)

# play war:
while len(player1) > 0 and len(player2) > 0:
    stock = []
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    # if card1["Power"] == card2["Power"]:
    #     player1.append(card1)
    #     player2.append(card2)
    #     print("=EQUAL \t %d \t %d \t" % (card1["Power"], card2["Power"]) + len(player1)*"*")
    # elif card1["Power"] > card2["Power"]:
    #     player1.append(card1)
    #     player1.append(card2)
    #     print("PLAY-1 \t %d \t %d \t" % (card1["Power"], card2["Power"]) + len(player1)*"*")
    # elif card1["Power"] < card2["Power"]:
    #     player2.append(card2)
    #     player2.append(card1)
    #     print("PLAY-2 \t %d \t %d \t" % (card1["Power"], card2["Power"]) + len(player2)*"*")

    if card1["Power"] == card2["Power"]:
        while card1["Power"] == card2["Power"]:
            print("The war is on!")
            print("Card's power is: \t %d \tand \t %d"% (card1["Power"], card2["Power"]))

            stock.append(card1)
            stock.append(card2)

            if len(player1) < 2:
                player2.extend(stock)
                player2.extend(player1)
                player1 = []
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2) * '*')
                break
            elif len(player2) < 2:
                player1.extend(stock)
                player1.extend(player2)
                player2 = []
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
                break
            # elif len(player1) == len(player2):
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stock.append(card1)
                stock.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1["Power"] > card2["Power"]:
                stock.append(card1)
                stock.append(card2)
                player1.extend(stock)
                print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
            else:
                stock.append(card1)
                stock.append(card2)
                player2.extend(stock)
                print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player2) * '*')

    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        print("PLAY-1 \t %d \t %d \t" % (card1["Power"], card2["Power"]) + len(player1)*"*")
    elif card1["Power"] < card2["Power"]:
        player2.append(card2)
        player2.append(card1)
        print("PLAY-2 \t %d \t %d \t" % (card1["Power"], card2["Power"]) + len(player2)*"*")

if len(player1) > 0:
    print("Player 1 won!")
else:
    print("Player 2 won!")