# omówienie i wyświetlenie tablicy ASCII:

# for i in range(32, 127):
#     print(i, chr(i))

# generowanie hasła:
import random

ints = range(33, 127)
password = ''

for i in range(16):
    password += chr(random.choice(ints))

print("Password is:", password)


# ZADANIA
print("-------------")
print("ZAD. 1. Generowanie rzutu kostka")
val_min = 1
val_max = 6
dice = random.randint(val_min, val_max)

if dice == 1:
    print(dice, ":")
    print("o")
elif dice == 2:
    print(dice, ":")
    print("\to")
    print("o")
elif dice == 3:
    print(dice, ":")
    print("\to")
    print("  o")
    print("o")
elif dice == 4:
    print(dice, ":")
    print("o o")
    print("o o")
elif dice == 5:
    print(dice, ":")
    print("o\to")
    print(" o")
    print("o\to")
elif dice == 6:
    print(dice, ":")
    print("o o")
    print("o o")
    print("o o")


print("-------------")
print("ZAD. 1. Generowanie rzutu kostka x5")

dices = []

for i in range(5):
    dices.append(random.randint(val_min, val_max))
dices.sort()
print(dices)