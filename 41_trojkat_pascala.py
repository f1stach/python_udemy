# budowa: nowa linia to suma dwoch wyzej znajdujacych sie elementow i jedynki po obu bokach

# szerokosc tekstu do wygenerowania:
width = 60

# liczba poziomow trojkata:
height = 7

# definiujemy element na szczycie:
numbers = [1]

# tworzymy trojkat takim podejsciem i kopiujemy na koniec for:
line = ""
for n in numbers:
    line = line + "%3d " % n
print(line.center(width)) # funkcja center wycentruje kazdy wiersz

# print(numbers)

# ustalamy ile linii ma byc
for i in range(height-1):
    # nowa linia za kazdym razem - jedynka na poczatku kazdej linii:
    newNumbers = [1]

    # przejdz przez wszystkie elementy w wierszu powyzej i dodaj parami
    position = 0
    while position < len(numbers) -1: # wykonaj o jeden mniej niz liczba wierszy (bo 1 na topie)
        # dodaj dwie liczby w wierszu i przejdz o pozycje dalej
        newNumbers.append(numbers[position] + numbers[position+1])
        position += 1

    # dodaj jedynke z góry do tablicy:
    newNumbers.append(1)

    # kopiujemy do nowej zmiennej zeby program widzial, ze od teraz ten wiersz jest gornym dla nowego wiersza
    numbers = newNumbers.copy()

    line = ""
    for n in numbers:
        line = line + "%3d " % n
    print(line.center(width))

    # print(numbers)
