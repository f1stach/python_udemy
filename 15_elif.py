age = 27
isDrunk = False
isRestrictedArea = False

if age < 18:
    print("You are too young")
elif isDrunk:
    print("You are drunk. No alcohol")
elif isRestrictedArea:
    print("Restricted, alco forbidden")
else:
    print("Ok, drink")

print("------------")
print("ZADANIE 1")

min_likes = 500
min_shares = 100
num_likes = 1300
num_shares = 150

if num_likes >= min_likes and num_shares >= min_shares:
    print("Ceny obnizamy o 10%")
elif num_likes < min_likes:
    print("Za malo polubien na obnizke cen")
elif num_shares < min_shares:
    print("Za mało udostepnien na obnizke cen")

print("ZADANIE 2")
isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print("Masz pan kupon na burgera")
elif isWeekend:
    print("Promocja tylko poza weekendem, ni mo kuponu")
else:
    print("Kupon bedzie jak kupisz pizze lub duzy napoj")