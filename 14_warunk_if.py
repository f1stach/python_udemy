age = 28

if age >= 18:
    print("You are adult and you can buy alcohol")
else:
    print("You are too young to buy alcohol")

isDrunk = False

if age >= 18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")

isRestrictedArea = False

if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are adult and you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")


# zadania
print("-------------------------")
print("ZADANIE 1")

min_likes = 500
min_shares = 100
num_likes = 1300
num_shares = 150

if num_likes >= min_likes and num_shares >= min_shares:
    print("Ceny obnizamy o 10%")
else:
    print("Za mało na obnizke cen")


print("ZADANIE 2")
isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = True

if (isPizzaOrdered or isBigDrinkOrdered) and isWeekend == False:
    print("Masz pan kupon na burgera")
else:
    print("Kupuj dalej, kuponu ni mo")


print("ZADANIE 3")
diskSize = 140
diskSizeUsed = 133
fileSize = 10

if fileSize < (diskSize - diskSizeUsed):
    print("File can be downloaded")
else:
    print("Not enough space")