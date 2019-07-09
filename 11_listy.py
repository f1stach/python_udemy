countries = ['FR', 'US', 'DE', 'RU']
countries[1] = 'GB'

print(countries[1])

countries.append('PL') # append - dodaje do konca listy
countries.insert(2, 'ES') # insert - wskazujemy miejsce i tam wstawiamy
countries.remove('RU') # remove - usun wskazany element
countries.sort() # sortowanie alfabetycznie
countries.reverse() # sortowanie od z do a
print(countries.pop(2)) # pop - zwraca wartosc wskazaną a nastepnie usuwa ja z listy
print(countries.index('PL')) # index - pokazuje czy element wystepuje i jezeli tak to na ktorej pozycji
# print(countries.index("US")) # nie ma elementu to wyjdzie error
print(countries.count('DE')) # count - ile jest takich elementów na liscie

newList = ['FI', 'SE']
countries.extend(newList) # extend - dodaje elementy do listy

countriesCopy = countries
# countriesCopy.clear() # mamy kopie, ale tylko w sensie innej nazwy dla listy. Miejsce w pamieci jest to samo
# wiec zeruje obie listy

print(countries)
print(countriesCopy)

# rozwiazaniem uzycie funkcji copy na liscie - powoduje, ze powstaje nowa kopia pamieci z elementami z pierwotnej listy
countriesCopy = countries.copy()
countriesCopy.clear() # tu czyscimy tylko kopię listy, oryginalna nietknieta

print(countries)
print(countriesCopy)


# ------------------------------------------------
# zadania:
hitsTitles = ['BROTHERS IN ARMS', 'BOHEMIAN RHAPSODY', 'STAIRWAY TO HEAVEN', 'RIDERS ON THE STORM', 'WISH YOU WERE HERE']

newTitles = ['CHILD IN TIME', 'AGAIN']
hitsTitles.extend(newTitles)

hitsTitles.insert(2, 'HOTEL CALIFORNIA')

hitsTitles.insert(0, 'THE SOUND OF SILENCE')

print(hitsTitles.index('HOTEL CALIFORNIA'))

hitsTitles.remove('HOTEL CALIFORNIA')

hitsTitles.insert(0, 'ENJOY THE SILENCE')

hitsToRead = hitsTitles.copy()

hitsToRead.reverse()
hitsToRead.sort()

hitsToRead.pop(0)
hitsToRead.pop(0)

additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']

hitsToRead.extend(additionalSongs)

print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))

hitsToRead.clear()

print(hitsTitles)
print(hitsToRead)