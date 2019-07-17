import random

# randint - losowanie liczby calkowitej w pelnym zakresie od 1 do 100
print("One random number:", random.randint(1,100))
print("\n")

# choice - tutaj zbior liczb do losowania, ale moze byc tez lista imion, adresow itp. Choice wybiera wartosc z listy
print("Choosing random number from a range:", random.choice(range(1,100)))
print("\n")

# randrange - prostsza forma niz dla choice
print("Choosing random number from a range - easier", random.randrange(1,100))
print("\n")

# shuffle - mieszanie listy losowo in place
list = ['John', 'Ann', 'Peter', 'Susan', 'Emily', 'Greg', 'Chris']
random.shuffle(list)
print("Reordered list:", list)
print("\n")

# random.random - losowanie liczby typu float od 0 do 1
print("Just a random float", random.random())
print("\n")


# ZADANIA
print("-----------------------")
print("ZAD. 1")

for i in range(1, 11):
    print(random.randint(i, 100))


print("-----------------------")
print("ZAD. 2")

number1 = random.randint(1,100)
counter = 1
number2 = random.randint(1,100)

print("Count number is", counter)
print("Generated number is", number2)

while number1 != number2:
    counter += 1
    number2 = random.randint(1,100)
    print("Count number is", counter)
    print("Generated number is", number2)

print("It took", counter, "trials to guess the number")
print("Number to be guessed was", number1)


print("-----------------------")
print("ZAD. 3")

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)

groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("----Grupa %d----" % groupNumber)
    print(countries[i])
