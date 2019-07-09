# range(20) generuje zbiór 20-u liczb. (1, 21, 2) - od 1 do 21 co 2.
# for number in range(1, 21, 2):
for number in range(1, 21):
    if number %2 == 0:
        print("Number %2d is %s" % (number, "even"))
    else:
        print("Number %2d is %s" % (number, "odd"))
#    print(number)


print("-----------------------")
print("ZADANIE 1")
string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for sign in range(1,11):
    print(sign, string_A)

print("-----------------------")
print("ZADANIE 2")

for sign in range(1,10):
        if sign %2 == 0:
            print(sign, string_B)
        else:
            print(sign, string_A)

print("-----------------------")
print("ZADANIE 3")

for number in range(1,10):
    print(number, "x"*number)

print("-----------------------")
print("ZADANIE 4")

for number in range(1,10):
    if number % 2 == 0:
        print(number, "x"*number)
    else:
        print(number, "o"*number)
